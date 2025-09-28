"""

<div class="grid cards" markdown>

- [:material-api:{ .lg .middle } __OpenAPI__](../assets/redoc.html?url=openapi_simple_html_display.json)

</div>


The goal of this extension is to illustrate the mechanism how cattle_grid
can be used to create a webpage displaying the public posts of its users.
The focus is on providing a working solution to key problems than on
providing the optimal solution.

An example of a feed is available at [@release](https://dev.bovine.social/@release).
The current scope is:

- Display actor and posts
- Correct redirecting behavior for easy use
- Display replies (todo)
- Export
- Import from compatible sources (todo)

This is not an independent solution. It relies on both the [context](./context.md) and
[simple_storage](./simple_storage.md) extension of cattle_grid.
"""

import logging
from uuid import uuid4

from bovine.activitystreams.utils import is_public
from sqlalchemy import select

from cattle_grid.account.account import account_for_actor
from cattle_grid.dependencies import (
    AccountExchangePublisher,
    ActivityExchangePublisher,
    CommittingSession,
    SqlSession,
)
from cattle_grid.dependencies.processing import FactoriesForActor

from cattle_grid.extensions import Extension
from cattle_grid.extensions.util import lifespan_for_sql_alchemy_base_class
from cattle_grid.manage.actor import ActorManager
from cattle_grid.model import ActivityMessage
from cattle_grid.model.exchange import UpdateActorMessage
from cattle_grid.model.exchange_update_actor import UpdateActionType, UpdateUrlAction
from cattle_grid.activity_pub.activity import actor_deletes_themselves

from .dependencies import PublishingActor
from .publisher import Publisher

from .config import HtmlDisplayConfiguration
from .database import (
    Base,
    ExportPermission,
    PublishedObject,
    PublishingActor as DBPublishingActor,
)
from .router import router
from .types import ExportTokenResponse, NameActorMessage


logger = logging.getLogger(__name__)

extension = Extension(
    name="simple html display",
    module=__name__,
    lifespan=lifespan_for_sql_alchemy_base_class(Base),
    config_class=HtmlDisplayConfiguration,
)
extension.rewrite_group_name = "html_display"
extension.rewrite_rules = {"publish_object": "html_display_publish_object"}
extension.include_router(router)


@extension.subscribe("html_display_publish_object")
async def html_publish_object(
    message: ActivityMessage,
    session: CommittingSession,
    actor: PublishingActor,
    config: extension.Config,  # type:ignore
    factories: FactoriesForActor,
    activity_publisher: ActivityExchangePublisher,
):
    """Publishes an object"""
    obj = message.data

    if not is_public(obj):
        await activity_publisher(
            ActivityMessage(actor=message.actor, data=obj),
            routing_key="publish_object",
        )
        return

    if obj.get("id"):
        raise ValueError("Object ID must not be set")

    if obj.get("attributedTo") != message.actor:
        raise ValueError("Actor must match object attributedTo")

    publisher = Publisher(actor, config)
    publisher.update_object(obj)

    session.add(PublishedObject(id=publisher.uuid, data=obj, actor=actor.actor))

    activity = factories[0].create(obj).build()

    await activity_publisher(
        ActivityMessage(actor=message.actor, data=activity),
        routing_key="publish_activity",
    )


@extension.subscribe("html_display_name")
async def name_actor(
    message: NameActorMessage,
    actor: PublishingActor,
    session: CommittingSession,
    activity_publisher: ActivityExchangePublisher,
    config: extension.Config,  # type:ignore
):
    """Sets the display name of the acotr"""
    if message.actor != actor.actor:
        raise Exception("Actor mismatch")

    actor.name = message.name

    await activity_publisher(
        UpdateActorMessage(
            actor=actor.actor,
            actions=[
                UpdateUrlAction(
                    action=UpdateActionType.add_url,
                    url=config.html_url(actor.actor, actor.name),
                    media_type="text/html",
                )
            ],
        ),
        routing_key="update_actor",
    )

    if config.automatically_add_users_to_group:
        manager = ActorManager(actor_id=actor.actor, session=session)
        await manager.add_to_group("html_display")


@extension.subscribe("html_display_export", replies=True)
async def export_create_token(
    actor: PublishingActor,
    session: CommittingSession,
    publisher: AccountExchangePublisher,
    config: extension.Config,  # type:ignore
):
    """Provides a token and download link for the export of stored objects

    The response is of type [cattle_grid.extensions.examples.html_display.types.ExportTokenResponse][] and
    send to `receive.NAME.response.trigger`."""
    token_uuid = uuid4()
    session.add(ExportPermission(publishing_actor=actor, one_time_token=token_uuid))

    account = await account_for_actor(session, actor.actor)

    if not account:
        raise Exception("Could not find account")

    await publisher(
        ExportTokenResponse(
            actor=actor.actor,
            token=str(token_uuid),
            export_url=config.html_url(actor.actor, actor.name)
            + f"/export?token={str(token_uuid)}",
        ),
        routing_key=f"receive.{account.name}.response.trigger",
    )


@extension.subscribe("outgoing.Delete")
async def outgoing_delete(
    message: ActivityMessage,
    session: SqlSession,
):
    activity = message.data.get("raw")
    if not isinstance(activity, dict):
        return
    if not actor_deletes_themselves(activity):
        return

    actor = await session.scalar(
        select(DBPublishingActor).where(DBPublishingActor.actor == message.actor)
    )
    if not actor:
        return

    logger.info("Deleting publishing actor with name %s", actor.name)

    await session.delete(actor)
    await session.flush()
