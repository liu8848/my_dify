import enum
import json

from flask_login import UserMixin

from extensions.ext_database import db
from models import StringUUID


class AccountStatus(str, enum.Enum):
    PENDING = 'pending'
    UNINITIALIZED = 'uninitialized'
    ACTIVE = 'active'
    BANNED = 'banned'
    CLOSED = 'closed'


class Account(UserMixin, db.Model):
    __tablename__ = 'accounts'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='account_pkey'),
        db.Index('account_email_idx', 'email')
    )

    # id = db.Column(StringUUID, server_default=db.text('uuid_generate_v4()'))
    id = db.Column(StringUUID, server_default=db.text('gen_random_uuid()'))
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    password_salt = db.Column(db.String(255), nullable=False)
    avatar = db.Column(db.String(255))
    interface_language = db.Column(db.String(255))
    interface_theme = db.Column(db.String(255))
    timezone = db.Column(db.String(255))
    last_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(255))
    last_active_at = db.Column(db.DateTime(), nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    status = db.Column(db.String(16), nullable=False, server_default=db.text("'active'::character varying"))
    initialized_at = db.Column(db.DateTime())
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))

    @property
    def is_password_set(self):
        return self.password is not None

    def get_status(self) -> AccountStatus:
        status_str = self.status
        return AccountStatus(status_str)

    @property
    def current_tenant(self):
        return self._current_tenant

    @current_tenant.setter
    def current_tenant(self, value):
        tenant = value
        ta = TenantAccountJoin.query.filter_by(tenant_id=tenant.id, account_id=self.id).first()
        if ta:
            tenant.current_role = ta.role
        else:
            tenant = None
        self._current_tenant = tenant

    @property
    def current_tenant_id(self):
        return self._current_tenant.id

    @current_tenant_id.setter
    def current_tenant_id(self, value):
        try:
            tenant_account_join = db.session.query(Tenant, TenantAccountJoin) \
                .filter(Tenant.id == value) \
                .filter(TenantAccountJoin.tenant_id == Tenant.id) \
                .filter(TenantAccountJoin.account_id == self.id) \
                .one_or_none()

            if tenant_account_join:
                tenant, ta = tenant_account_join
                tenant.current_role = ta.role
            else:
                tenant = None
        except:
            tenant = None
        self._current_tenant = tenant


class Tenant(db.Model):
    __tablename__ = 'tenants'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='tenant_pkey'),
    )

    id = db.Column(StringUUID, server_default=db.text('gen_random_uuid()'))
    name = db.Column(db.String(255), nullable=False)
    encrypt_public_key = db.Column(db.Text)
    plan = db.Column(db.String(255), nullable=False, server_default=db.text("'basic'::character varying"))
    status = db.Column(db.String(255), nullable=False, server_default=db.text("'normal'::character varying"))
    custom_config = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))

    def get_accounts(self) -> list[db.Model]:
        Account = db.Model
        return db.session.query(Account).filter(
            Account.id == TenantAccountJoin.account_id,
            TenantAccountJoin.tenant_id == self.id
        ).all()

    @property
    def custom_config_dict(self) -> dict:
        return json.loads(self.custom_config) if self.custom_config else {}

    @custom_config_dict.setter
    def custom_config_dict(self, value: dict):
        self.custom_config = json.dumps(value)


class TenantAccountJoin(db.Model):
    __tablename__ = 'tenant_account_joins'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='tenant_account_joins_pkey'),
        db.Index('tenant_account_join_account_id_idx', 'account_id'),
        db.Index('tenant_account_join_tenant_id_idx', 'tenant_id'),
        db.UniqueConstraint('tenant_id', 'account_id', name='unique_tenant_account_join'),
    )

    id = db.Column(StringUUID, server_default=db.text('gen_random_uuid()'))
    tenant_id = db.Column(StringUUID, nullable=False)
    account_id = db.Column(StringUUID, nullable=False)
    current = db.Column(db.Boolean, nullable=False, server_default=db.text('false'))
    role = db.Column(db.String(16), nullable=False, server_default='normal')
    invited_by = db.Column(StringUUID, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
