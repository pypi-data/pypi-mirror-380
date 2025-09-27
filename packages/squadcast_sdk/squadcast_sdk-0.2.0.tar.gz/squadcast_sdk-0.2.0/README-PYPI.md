# openapi

Developer-friendly & type-safe Python SDK specifically catered to leverage *openapi* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=openapi&utm_campaign=python"><img src="https://www.speakeasy.com/assets/badges/built-by-speakeasy.svg" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/swo/incident-response). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary


<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [openapi](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/#openapi)
  * [SDK Installation](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/#sdk-installation)
  * [IDE Support](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/#ide-support)
  * [SDK Example Usage](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/#sdk-example-usage)
  * [Authentication](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/#authentication)
  * [Available Resources and Operations](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/#available-resources-and-operations)
  * [File uploads](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/#file-uploads)
  * [Retries](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/#retries)
  * [Error Handling](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/#error-handling)
  * [Server Selection](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/#server-selection)
  * [Custom HTTP Client](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/#custom-http-client)
  * [Resource Management](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/#resource-management)
  * [Debugging](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/#debugging)
* [Development](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/#development)
  * [Maturity](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/#maturity)
  * [Contributions](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add squadcast_sdk
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install squadcast_sdk
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add squadcast_sdk
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from squadcast_sdk python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "squadcast_sdk",
# ]
# ///

from squadcast_sdk import SquadcastSDK

sdk = SquadcastSDK(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.analytics.get_org_analytics(from_="<value>", to="<value>")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from squadcast_sdk import SquadcastSDK

async def main():

    async with SquadcastSDK(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as ss_client:

        res = await ss_client.analytics.get_org_analytics_async(from_="<value>", to="<value>")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type | Scheme      |
| ------------- | ---- | ----------- |
| `bearer_auth` | http | HTTP Bearer |

To authenticate with the API the `bearer_auth` parameter must be set when initializing the SDK client instance. For example:
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.analytics.get_org_analytics(from_="<value>", to="<value>")

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [additional_responders](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/additionalresponders/README.md)

* [remove](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/additionalresponders/README.md#remove) - Remove Additional Responders

### [analytics](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/analytics/README.md)

* [get_org_analytics](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/analytics/README.md#get_org_analytics) - Get Org level analytics
* [get_team](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/analytics/README.md#get_team) - Get Team level analytics

### [communication_cards](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/communicationcards/README.md)

* [get_all](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/communicationcards/README.md#get_all) - Get All Communication Card

### [component_groups](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/componentgroups/README.md)

* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/componentgroups/README.md#create) - Create Component Group

### [components](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/components/README.md)

* [list](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/components/README.md#list) - List Components
* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/components/README.md#create) - Create Component
* [get_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/components/README.md#get_by_id) - Get Component By ID
* [update_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/components/README.md#update_by_id) - Update Component By ID

### [dedup_keys](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/dedupkeys/README.md)

* [list_by_service](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/dedupkeys/README.md#list_by_service) - Get All Dedup Key Overlay by Service
* [delete](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/dedupkeys/README.md#delete) - Delete Dedup Key Overlay

### [escalation_policies](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/escalationpoliciessdk/README.md)

* [get_by_team](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/escalationpoliciessdk/README.md#get_by_team) - Get Escalation Policy By team
* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/escalationpoliciessdk/README.md#create) - Create Escalation Policies
* [remove](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/escalationpoliciessdk/README.md#remove) - Remove Escalation Policy
* [get_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/escalationpoliciessdk/README.md#get_by_id) - Get Escalation Policy By ID
* [update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/escalationpoliciessdk/README.md#update) - Update Escalation Policy

### [export_schedule](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/exportschedule/README.md)

* [refresh_ical_link](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/exportschedule/README.md#refresh_ical_link) - Refresh Schedule ICal Link

### [exports](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/exports/README.md)

* [get_details](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/exports/README.md#get_details) - Get Export Details

### [extensions](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/extensions/README.md)


#### [extensions.ms_teams](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/msteams1/README.md)

* [get_config](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/msteams1/README.md#get_config) - Get MSTeams Config

#### [extensions.msteams](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/msteams2/README.md)

* [create_or_update_config](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/msteams2/README.md#create_or_update_config) - Create Or Update MSTeams Configuration

#### [extensions.webhooks](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/extensionswebhooks/README.md)

* [get_all](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/extensionswebhooks/README.md#get_all) - Get All Webhooks

### [global_event_rules](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/globaleventrules/README.md)

* [list](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/globaleventrules/README.md#list) - List Global Event Rules
* [create_rule](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/globaleventrules/README.md#create_rule) - Create Global Event Rule
* [delete_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/globaleventrules/README.md#delete_by_id) - Delete Global Event Rule by ID
* [get_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/globaleventrules/README.md#get_by_id) - Get Global Event Rule by ID
* [update_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/globaleventrules/README.md#update_by_id) - Update Global Event Rule by ID

#### [global_event_rules.rulesets](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/globaleventrulesrulesets/README.md)

* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/globaleventrulesrulesets/README.md#create) - Create Ruleset
* [delete](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/globaleventrulesrulesets/README.md#delete) - Delete GER Ruleset
* [get](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/globaleventrulesrulesets/README.md#get) - Get Ruleset
* [update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/globaleventrulesrulesets/README.md#update) - Update Ruleset

#### [global_event_rules.rulesets.rules](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/rulesetsrules/README.md)

* [list](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/rulesetsrules/README.md#list) - List Ruleset Rules
* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/rulesetsrules/README.md#create) - Create Rule
* [get_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/rulesetsrules/README.md#get_by_id) - Get Rule by ID
* [update_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/rulesetsrules/README.md#update_by_id) - Update Rule by ID
* [reorder](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/rulesetsrules/README.md#reorder) - Reorder Ruleset By Index

### [global_oncall_reminder_rules](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/globaloncallreminderrulessdk/README.md)

* [delete](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/globaloncallreminderrulessdk/README.md#delete) - Delete Global Oncall Reminder Rules
* [get](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/globaloncallreminderrulessdk/README.md#get) - Get Global Oncall Reminder Rules
* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/globaloncallreminderrulessdk/README.md#create) - Create Global Oncall Reminder Rules
* [update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/globaloncallreminderrulessdk/README.md#update) - Update Global Oncall Reminder Rules

### [incidents](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidents/README.md)

* [bulk_acknowledge](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidents/README.md#bulk_acknowledge) - Bulk Acknowledge Incidents
* [export_incidents](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidents/README.md#export_incidents) - Incident Export
* [bulk_update_priority](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidents/README.md#bulk_update_priority) - Bulk Incidents Priority Update
* [bulk_resolve](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidents/README.md#bulk_resolve) - Bulk Resolve Incidents
* [get_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidents/README.md#get_by_id) - Get Incident by ID
* [acknowledge](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidents/README.md#acknowledge) - Acknowledge Incident
* [mark_slo_false_positive](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidents/README.md#mark_slo_false_positive) - Mark Incident SLO False Positive
* [update_priority](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidents/README.md#update_priority) - Incident Priority Update
* [reassign](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidents/README.md#reassign) - Reassign Incident
* [resolve](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidents/README.md#resolve) - Resolve Incident
* [get_status_by_request_ids](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidents/README.md#get_status_by_request_ids) - Get Incidents Status By RequestIDs

#### [incidents.actions](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidentsactions/README.md)

* [rebuild_circleci_project](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidentsactions/README.md#rebuild_circleci_project) - Rebuild a Project In CircleCI

#### [incidents.actions.jira](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/jira/README.md)

* [create_ticket](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/jira/README.md#create_ticket) - Create a Ticket on Jira Cloud

#### [incidents.actions.service_now](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/servicenow/README.md)

* [create_incident](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/servicenow/README.md#create_incident) - Create an Incident in ServiceNow

#### [incidents.actions.webhook](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/webhook/README.md)

* [trigger](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/webhook/README.md#trigger) - Trigger a Webhook Manually

#### [incidents.additional_responders](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidentsadditionalresponders/README.md)

* [list](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidentsadditionalresponders/README.md#list) - Get Additional Responders
* [add](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidentsadditionalresponders/README.md#add) - Add Additional Responders

#### [incidents.auto_pause_transient_alerts](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/autopausetransientalerts/README.md)

* [mark_as_not_transient](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/autopausetransientalerts/README.md#mark_as_not_transient) - Mark as Not Transient
* [mark_as_transient](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/autopausetransientalerts/README.md#mark_as_transient) - Mark as Transient

#### [incidents.communication_card](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/communicationcard/README.md)

* [create_slack_channel](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/communicationcard/README.md#create_slack_channel) - Create Slack Channel in Communication Card
* [archive_slack_channel](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/communicationcard/README.md#archive_slack_channel) - Archive Slack Channel

#### [incidents.communication_cards](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidentscommunicationcards/README.md)

* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidentscommunicationcards/README.md#create) - Create Communication Card
* [delete](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidentscommunicationcards/README.md#delete) - Delete Communication Card
* [update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidentscommunicationcards/README.md#update) - Update Communication Card

#### [incidents.events](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/events/README.md)

* [get](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/events/README.md#get) - Get Incident Events

#### [incidents.export](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidentsexport/README.md)

* [export_async](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidentsexport/README.md#export_async) - Incident Export Async

#### [incidents.incident_actions](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidentactions/README.md)

* [create_jira_ticket](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidentactions/README.md#create_jira_ticket) - Create a Ticket on Jira Server

#### [incidents.notes](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/notes/README.md)

* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/notes/README.md#create) - Create Notes
* [list](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/notes/README.md#list) - Get All Notes
* [delete](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/notes/README.md#delete) - Delete Note
* [update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/notes/README.md#update) - Update Note

#### [incidents.postmortems](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidentspostmortems/README.md)

* [remove](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidentspostmortems/README.md#remove) - Delete Postmortem By Incident
* [get_by_incident](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidentspostmortems/README.md#get_by_incident) - Get Postmortem By Incident
* [update_by_incident](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidentspostmortems/README.md#update_by_incident) - Update Postmortem By Incident

#### [incidents.snooze_notifications](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidentssnoozenotifications/README.md)

* [unsnooze](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidentssnoozenotifications/README.md#unsnooze) - Unsnooze Incident Notifications

#### [incidents.tags](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidentstags/README.md)

* [update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidentstags/README.md#update) - Update Tag
* [append](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/incidentstags/README.md#append) - Append Tag

### [issues](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/issues/README.md)

* [delete_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/issues/README.md#delete_by_id) - Delete Issue By ID
* [update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/issues/README.md#update) - Update Issue
* [list](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/issues/README.md#list) - List Status Page Issue States

### [maintenances](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/maintenances/README.md)

* [delete](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/maintenances/README.md#delete) - Delete Maintenance By ID
* [update_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/maintenances/README.md#update_by_id) - Update Maintenance By ID

### [overlays](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/overlays/README.md)


#### [overlays.dedup_key](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/dedupkey/README.md)

* [get_for_alert_source](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/dedupkey/README.md#get_for_alert_source) - Get Dedup Key Overlay for Alert Source

### [overrides](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/overrides/README.md)

* [remove](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/overrides/README.md#remove) - Delete Schedule Override
* [get_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/overrides/README.md#get_by_id) - Get Override by ID

### [postmortems](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/postmortemssdk/README.md)

* [get_all](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/postmortemssdk/README.md#get_all) - Get All Postmortems
* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/postmortemssdk/README.md#create) - Create Postmortem

### [rotations](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/rotations/README.md)

* [list_by_schedule](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/rotations/README.md#list_by_schedule) - List Schedule Rotations
* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/rotations/README.md#create) - Create Rotation
* [delete](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/rotations/README.md#delete) - Delete Rotation
* [get_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/rotations/README.md#get_by_id) - Get Schedule Rotation by ID
* [update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/rotations/README.md#update) - Update Rotation
* [get_participants](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/rotations/README.md#get_participants) - Get Rotation Participants
* [update_participants](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/rotations/README.md#update_participants) - Update Rotation Participants

### [rules](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/rules/README.md)

* [delete_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/rules/README.md#delete_by_id) - Delete Rule by ID

### [rulesets](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/rulesets/README.md)

* [reorder](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/rulesets/README.md#reorder) - Reorder Ruleset

### [runbooks](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/runbookssdk/README.md)

* [attach](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/runbookssdk/README.md#attach) - Attach Runbooks
* [get_all_by_team](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/runbookssdk/README.md#get_all_by_team) - Get All Runbooks By Team
* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/runbookssdk/README.md#create) - Create Runbook
* [delete](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/runbookssdk/README.md#delete) - Remove Runbook
* [get_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/runbookssdk/README.md#get_by_id) - Get Runbook By ID
* [update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/runbookssdk/README.md#update) - Update Runbook

### [schedules](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/schedulessdk/README.md)

* [list](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/schedulessdk/README.md#list) - List Schedules
* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/schedulessdk/README.md#create) - Create Schedule
* [delete](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/schedulessdk/README.md#delete) - Delete Schedule
* [get_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/schedulessdk/README.md#get_by_id) - Get Schedule by ID
* [update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/schedulessdk/README.md#update) - Update Schedule
* [pause_resume](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/schedulessdk/README.md#pause_resume) - Pause/Resume Schedule
* [change_timezone](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/schedulessdk/README.md#change_timezone) - Change Timezone
* [clone](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/schedulessdk/README.md#clone) - Clone Schedule
* [get_ical_link](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/schedulessdk/README.md#get_ical_link) - Get Schedule ICal Link
* [create_ical_link](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/schedulessdk/README.md#create_ical_link) - Create Schedule ICal Link

#### [schedules.export](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/schedulesexport/README.md)

* [delete_ical_link](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/schedulesexport/README.md#delete_ical_link) - Delete ICal Link

#### [schedules.overrides](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/schedulesoverrides/README.md)

* [list](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/schedulesoverrides/README.md#list) - List Overrides
* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/schedulesoverrides/README.md#create) - Create Schedule Override
* [update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/schedulesoverrides/README.md#update) - Update Schedule Override

### [services](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/servicessdk/README.md)

* [get_all](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/servicessdk/README.md#get_all) - Get All Services
* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/servicessdk/README.md#create) - Create Service
* [get_by_name](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/servicessdk/README.md#get_by_name) - Get Services By Name
* [get_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/servicessdk/README.md#get_by_id) - Get Service By ID
* [update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/servicessdk/README.md#update) - Update Service
* [delete](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/servicessdk/README.md#delete) - Delete Service
* [update_apta_config](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/servicessdk/README.md#update_apta_config) - Auto Pause Transient Alerts (APTA)
* [create_or_update_iag_config](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/servicessdk/README.md#create_or_update_iag_config) - Intelligent Alert Grouping (IAG)
* [update_notification_delay_config](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/servicessdk/README.md#update_notification_delay_config) - Delayed Notification Config

#### [services.deduplication_rules](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/deduplicationrules/README.md)

* [get](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/deduplicationrules/README.md#get) - Get Deduplication Rules
* [create_or_update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/deduplicationrules/README.md#create_or_update) - Create or Update Deduplication Rules

#### [services.dependencies](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/dependencies/README.md)

* [create_or_update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/dependencies/README.md#create_or_update) - Create or Update Dependencies

#### [services.extensions](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/servicesextensions/README.md)

* [update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/servicesextensions/README.md#update) - Update Slack Extension

#### [services.maintenance](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/maintenance/README.md)

* [create_or_update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/maintenance/README.md#create_or_update) - Create or Update Maintenance Mode

#### [services.maintenance_mode](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/maintenancemode/README.md)

* [get](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/maintenancemode/README.md#get) - Get Maintenance Mode

#### [services.overlay](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/overlay/README.md)

* [get_optin_for_key_based_deduplication](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/overlay/README.md#get_optin_for_key_based_deduplication) - Get Opt-in for Key Based Deduplication for a service
* [optin_for_key_based_deduplication](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/overlay/README.md#optin_for_key_based_deduplication) - Opt-in for Key Based Deduplication for a service

#### [services.overlay.custom_content_templates](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/overlaycustomcontenttemplates/README.md)

* [get_all](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/overlaycustomcontenttemplates/README.md#get_all) - Get All Custom Content Template Overlay by Service
* [create_or_update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/overlaycustomcontenttemplates/README.md#create_or_update) - Create or Update Notification Template Overlay

#### [services.overlays](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/servicesoverlays/README.md)

* [render_dedup_key](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/servicesoverlays/README.md#render_dedup_key) - Render Dedup Key template

#### [services.overlays.custom_content_templates](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/overlayscustomcontenttemplates/README.md)

* [render](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/overlayscustomcontenttemplates/README.md#render) - Render Custom Content Overlay
* [delete](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/overlayscustomcontenttemplates/README.md#delete) - Delete Notification Template Overlay
* [get](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/overlayscustomcontenttemplates/README.md#get) - Get Custom Content Template Overlay

#### [services.overlays.dedup_key](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/servicesdedupkey/README.md)

* [update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/servicesdedupkey/README.md#update) - Update Dedup Key Overlay

#### [services.routing_rules](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/routingrules/README.md)

* [get](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/routingrules/README.md#get) - Get Routing Rules
* [create_or_update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/routingrules/README.md#create_or_update) - Create or Update Routing Rules

#### [services.suppression_rules](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/suppressionrules/README.md)

* [get](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/suppressionrules/README.md#get) - Get Suppression Rules
* [create_or_update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/suppressionrules/README.md#create_or_update) - Create or Update Suppression Rules

#### [services.tagging_rules](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/taggingrules/README.md)

* [get](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/taggingrules/README.md#get) - Get Tagging Rules
* [create_or_update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/taggingrules/README.md#create_or_update) - Create or Update Tagging Rules

### [slos](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/slossdk/README.md)

* [list_all](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/slossdk/README.md#list_all) - Get All SLOs
* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/slossdk/README.md#create) - Create SLO
* [update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/slossdk/README.md#update) - Update SLO
* [remove](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/slossdk/README.md#remove) - Remove SLO
* [get](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/slossdk/README.md#get) - Get SLO By ID
* [mark_affected](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/slossdk/README.md#mark_affected) - Mark SLO Affected

#### [slos.false_positive](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/falsepositive/README.md)

* [mark](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/falsepositive/README.md#mark) - Mark SLO False Positive

### [snooze_notifications](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/snoozenotifications/README.md)

* [snooze](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/snoozenotifications/README.md#snooze) - Snooze Incident Notifications


### [squads](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/squadssdk/README.md)

* [list](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/squadssdk/README.md#list) - Get All Squads
* [get_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/squadssdk/README.md#get_by_id) - Get Squad By ID
* [update_v4](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/squadssdk/README.md#update_v4) - Update Squad
* [remove_member](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/squadssdk/README.md#remove_member) - Remove Squad Member
* [squads_delete_squad](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/squadssdk/README.md#squads_delete_squad) - Delete Squad

#### [squads.members](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/squadsmembers/README.md)

* [update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/squadsmembers/README.md#update) - Update Squad Member

### [squads_v4](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/squadsv4/README.md)

* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/squadsv4/README.md#create) - Create Squad
* [update_name](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/squadsv4/README.md#update_name) - Update Squad Name

### [status_pages](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagessdk1/README.md)

* [list](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagessdk1/README.md#list) - List Status Pages
* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagessdk1/README.md#create) - Create Status Page
* [delete_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagessdk1/README.md#delete_by_id) - Delete Status Page By ID
* [get_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagessdk1/README.md#get_by_id) - Get Status Page By ID
* [update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagessdk1/README.md#update) - Update Status Page By ID
* [list_statuses](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagessdk1/README.md#list_statuses) - List Status Page Statuses

#### [status_pages.component_groups](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagescomponentgroups/README.md)

* [list](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagescomponentgroups/README.md#list) - List Component Groups
* [remove_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagescomponentgroups/README.md#remove_by_id) - Delete Component Group By ID
* [get_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagescomponentgroups/README.md#get_by_id) - Get Component Group By ID

#### [status_pages.components](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagescomponents/README.md)

* [delete_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagescomponents/README.md#delete_by_id) - Delete Component By ID

#### [status_pages.issues](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagesissues/README.md)

* [list](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagesissues/README.md#list) - List Issues
* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagesissues/README.md#create) - Create Issue
* [get_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagesissues/README.md#get_by_id) - Get Issue By ID

#### [status_pages.maintenances](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagesmaintenances1/README.md)

* [list](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagesmaintenances1/README.md#list) - List Maintenances
* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagesmaintenances1/README.md#create) - Create Maintenance

### [statuspages](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagessdk2/README.md)


#### [statuspages.maintenances](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagesmaintenances2/README.md)

* [get_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/statuspagesmaintenances2/README.md#get_by_id) - Get Maintenance By ID

### [subscribers](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/subscribers/README.md)

* [list](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/subscribers/README.md#list) - List Subscribers

### [teams](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/teams/README.md)

* [get_all](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/teams/README.md#get_all) - Get All Teams
* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/teams/README.md#create) - Create Team
* [get](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/teams/README.md#get) - Get Team By ID
* [update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/teams/README.md#update) - Update Team
* [remove](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/teams/README.md#remove) - Remove Team
* [add_bulk_member](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/teams/README.md#add_bulk_member) - Add Bulk Team Member
* [remove_member](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/teams/README.md#remove_member) - Remove Team Member
* [update_member](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/teams/README.md#update_member) - Update Team Member
* [remove_role](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/teams/README.md#remove_role) - Remove Team Role

#### [teams.members](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/teamsmembers/README.md)

* [list](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/teamsmembers/README.md#list) - Get All Team Members
* [add](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/teamsmembers/README.md#add) - Add Team Member

#### [teams.roles](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/roles/README.md)

* [get_all](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/roles/README.md#get_all) - Get All Team Roles
* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/roles/README.md#create) - Create Team Role
* [update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/roles/README.md#update) - Update Team Role

### [users](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/users/README.md)

* [get_all](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/users/README.md#get_all) - Get All Users
* [add](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/users/README.md#add) - Add User
* [update_org_level_permissions](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/users/README.md#update_org_level_permissions) - Update Org Level Permissions
* [delete](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/users/README.md#delete) - Delete User
* [get_roles](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/users/README.md#get_roles) - Get User Roles
* [remove_from_org](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/users/README.md#remove_from_org) - Remove User From Org
* [get_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/users/README.md#get_by_id) - Get User By ID
* [update_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/users/README.md#update_by_id) - Update User by userID

#### [users.api_token](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/apitoken/README.md)

* [remove](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/apitoken/README.md#remove) - Remove Token

#### [users.api_tokens](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/apitokens/README.md)

* [list](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/apitokens/README.md#list) - Get All Tokens
* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/apitokens/README.md#create) - Create Token

### [webforms](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/webformssdk/README.md)

* [list](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/webformssdk/README.md#list) - Get All Webforms
* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/webformssdk/README.md#create) - Create Webform
* [update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/webformssdk/README.md#update) - Update Webform
* [remove](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/webformssdk/README.md#remove) - Remove Webform
* [get_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/webformssdk/README.md#get_by_id) - Get Webform By ID

### [webhooks](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/webhooks/README.md)

* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/webhooks/README.md#create) - Create Webhook
* [delete](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/webhooks/README.md#delete) - Delete Webhook
* [get_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/webhooks/README.md#get_by_id) - Get Webhook By ID
* [update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/webhooks/README.md#update) - Update Webhook

### [workflows](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/workflowssdk/README.md)

* [list](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/workflowssdk/README.md#list) - List Workflows
* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/workflowssdk/README.md#create) - Create Workflow
* [bulk_enable_disable](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/workflowssdk/README.md#bulk_enable_disable) - Bulk Enable/Disable Workflows
* [delete](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/workflowssdk/README.md#delete) - Delete Workflow
* [get_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/workflowssdk/README.md#get_by_id) - Get Workflow By ID
* [update](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/workflowssdk/README.md#update) - Update Workflow
* [update_actions_order](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/workflowssdk/README.md#update_actions_order) - Update Actions Order
* [delete_action](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/workflowssdk/README.md#delete_action) - Delete Workflow Action
* [update_action](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/workflowssdk/README.md#update_action) - Update Workflow Action
* [enable_disable](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/workflowssdk/README.md#enable_disable) - Enable/Disable Workflow

#### [workflows.actions](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/workflowsactions/README.md)

* [create](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/workflowsactions/README.md#create) - Create Action
* [get_by_id](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/workflowsactions/README.md#get_by_id) - Get Workflow Action By ID

#### [workflows.logs](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/logs/README.md)

* [get](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/docs/sdks/logs/README.md#get) - Get Workflow Logs

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.escalation_policies.update(escalation_policy_id="<id>", v3_escalation_policies_update_escalation_policy_request=open("example.file", "rb"))

    # Handle response
    print(res)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from squadcast_sdk import SquadcastSDK
from squadcast_sdk.utils import BackoffStrategy, RetryConfig


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.analytics.get_org_analytics(from_="<value>", to="<value>",
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from squadcast_sdk import SquadcastSDK
from squadcast_sdk.utils import BackoffStrategy, RetryConfig


with SquadcastSDK(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.analytics.get_org_analytics(from_="<value>", to="<value>")

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`SquadcastSDKError`](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/./src/squadcast_sdk/errors/squadcastsdkerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/#error-classes). |

### Example
```python
from squadcast_sdk import SquadcastSDK, errors


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:
    res = None
    try:

        res = ss_client.analytics.get_org_analytics(from_="<value>", to="<value>")

        # Handle response
        print(res)


    except errors.SquadcastSDKError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.BadRequestError):
            print(e.data.meta)  # models.CommonV3ErrorMeta
```

### Error Classes
**Primary errors:**
* [`SquadcastSDKError`](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/./src/squadcast_sdk/errors/squadcastsdkerror.py): The base class for HTTP error responses.
  * [`PaymentRequiredError`](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/./src/squadcast_sdk/errors/paymentrequirederror.py): Client error. Status code `402`. *
  * [`ForbiddenError`](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/./src/squadcast_sdk/errors/forbiddenerror.py): Access is forbidden. Status code `403`. *
  * [`NotFoundError`](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/./src/squadcast_sdk/errors/notfounderror.py): The server cannot find the requested resource. Status code `404`. *
  * [`ConflictError`](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/./src/squadcast_sdk/errors/conflicterror.py): The request conflicts with the current state of the server. Status code `409`. *
  * [`UnprocessableEntityError`](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/./src/squadcast_sdk/errors/unprocessableentityerror.py): Client error. Status code `422`. *
  * [`InternalServerError`](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/./src/squadcast_sdk/errors/internalservererror.py): Server error. Status code `500`. *
  * [`BadGatewayError`](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/./src/squadcast_sdk/errors/badgatewayerror.py): Server error. Status code `502`. *
  * [`ServiceUnavailableError`](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/./src/squadcast_sdk/errors/serviceunavailableerror.py): Service unavailable. Status code `503`. *
  * [`GatewayTimeoutError`](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/./src/squadcast_sdk/errors/gatewaytimeouterror.py): Server error. Status code `504`. *
  * [`UnauthorizedError`](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/./src/squadcast_sdk/errors/unauthorizederror.py): Access is unauthorized. Status code `401`. *
  * [`BadRequestError`](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/./src/squadcast_sdk/errors/badrequesterror.py): The server could not understand the request due to invalid syntax. Status code `400`. *

<details><summary>Less common errors (8)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`SquadcastSDKError`](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/./src/squadcast_sdk/errors/squadcastsdkerror.py)**:
* [`CommonV4Error`](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/./src/squadcast_sdk/errors/commonv4error.py): The server could not understand the request due to invalid syntax. Applicable to 32 of 225 methods.*
* [`ResponseBodyError1`](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/./src/squadcast_sdk/errors/responsebodyerror1.py): Represents a CircleCI error response for a 400 status code. Status code `400`. Applicable to 1 of 225 methods.*
* [`ResponseBodyError2`](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/./src/squadcast_sdk/errors/responsebodyerror2.py): Represents a CircleCI error response for a 400 status code. Status code `400`. Applicable to 1 of 225 methods.*
* [`ResponseValidationError`](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/./src/squadcast_sdk/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](https://github.com/SquadcastHub/squadcast-sdk-python/blob/master/squadcastv1/#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    server_url="https://api.squadcast.com",
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.analytics.get_org_analytics(from_="<value>", to="<value>")

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from squadcast_sdk import SquadcastSDK
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = SquadcastSDK(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from squadcast_sdk import SquadcastSDK
from squadcast_sdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = SquadcastSDK(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `SquadcastSDK` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from squadcast_sdk import SquadcastSDK
def main():

    with SquadcastSDK(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as ss_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with SquadcastSDK(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as ss_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from squadcast_sdk import SquadcastSDK
import logging

logging.basicConfig(level=logging.DEBUG)
s = SquadcastSDK(debug_logger=logging.getLogger("squadcast_sdk"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=openapi&utm_campaign=python)
