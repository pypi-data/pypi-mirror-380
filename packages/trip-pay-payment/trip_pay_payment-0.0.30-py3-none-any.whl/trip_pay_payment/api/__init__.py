# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from trip_pay_payment.api.account_api import AccountApi
    from trip_pay_payment.api.account_mappings_api import AccountMappingsApi
    from trip_pay_payment.api.affiliate_api import AffiliateApi
    from trip_pay_payment.api.agent_api import AgentApi
    from trip_pay_payment.api.application_api import ApplicationApi
    from trip_pay_payment.api.contract_api import ContractApi
    from trip_pay_payment.api.managing_entity_api import ManagingEntityApi
    from trip_pay_payment.api.mapping_api import MappingApi
    from trip_pay_payment.api.notification_api import NotificationApi
    from trip_pay_payment.api.ping_api import PingApi
    from trip_pay_payment.api.webhook_api import WebhookApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from trip_pay_payment.api.account_api import AccountApi
from trip_pay_payment.api.account_mappings_api import AccountMappingsApi
from trip_pay_payment.api.affiliate_api import AffiliateApi
from trip_pay_payment.api.agent_api import AgentApi
from trip_pay_payment.api.application_api import ApplicationApi
from trip_pay_payment.api.contract_api import ContractApi
from trip_pay_payment.api.managing_entity_api import ManagingEntityApi
from trip_pay_payment.api.mapping_api import MappingApi
from trip_pay_payment.api.notification_api import NotificationApi
from trip_pay_payment.api.ping_api import PingApi
from trip_pay_payment.api.webhook_api import WebhookApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
