from typing import Optional

from flask import current_app, request

from extensions.ext_database import db
from models import StringUUID
from models.account import Tenant
from models.entities.app.app_model_config import AppModelConfig
from models.entities.app.site import Site
from models.entities.workflow.workflow import Workflow


class App(db.Model):
    __tablename__ = 'apps'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='app_pkey'),
        db.Index('app_tenant_id_idx', 'tenant_id'),
    )

    id = db.Column(StringUUID, server_default=db.text('gen_random_uuid()'))
    tenant_id = db.Column(StringUUID, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False, server_default=db.text("''::character varying"))
    mode = db.Column(db.String(255), nullable=False)
    icon = db.Column(db.String(255))
    icon_background = db.Column(db.String(255))
    app_model_config_id = db.Column(StringUUID, nullable=True)
    workflow_id = db.Column(StringUUID, nullable=True)
    status = db.Column(db.String(255), nullable=False, server_default=db.text("'normal'::character varying"))
    enable_site = db.Column(db.Boolean, nullable=False)
    enable_api = db.Column(db.Boolean, nullable=False)
    api_rpm = db.Column(db.Integer, nullable=False, server_default=db.text('0'))
    api_rph = db.Column(db.Integer, nullable=False, server_default=db.text('0'))
    is_demo = db.Column(db.Boolean, nullable=False, server_default=db.text('false'))
    is_public = db.Column(db.Boolean, nullable=False, server_default=db.text('false'))
    is_universal = db.Column(db.Boolean, nullable=False, server_default=db.text('false'))
    create_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))

    @property
    def desc_or_prompt(self):
        if self.description:
            return self.description
        else:
            app_model_config = self.app_model_config
            if app_model_config:
                return app_model_config.pre_prompt
            else:
                return ''

    @property
    def site(self):
        site = db.session.query(Site).filter(Site.app_id == self.id).first()
        return site

    @property
    def app_model_config(self) -> Optional['AppModelConfig']:
        if self.app_model_config_id:
            return db.session.query(AppModelConfig).filter(AppModelConfig.id == self.app_model_config_id).first()
        return None

    @property
    def workflow(self) -> Optional['Workflow']:
        if self.workflow_id:
            from ..workflow.workflow import Workflow
            return db.session.query(Workflow).filter(Workflow.id == self.workflow_id).first()
        return None

    @property
    def api_base_url(self):
        return (current_app.config['SERVICE_API_URL'] if current_app.config[
            'SERVICE_API_URL'] else request.base_url).rstrip('/') + '/v1'

    @property
    def tenant(self):
        tenant = db.session.query(Tenant).filter(Tenant.id == self.tenant_id).first()
        return tenant

