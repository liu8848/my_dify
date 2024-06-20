from flask import current_app, request

from extensions.ext_database import db
from libs.helper import generate_string
from models import StringUUID


class Site(db.Model):
    __tablename__ = 'sites'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='site_pkey'),
        db.Index('site_app_id_idx', 'app_id'),
        db.Index('site_code_idx', 'code', 'status'),
    )

    id = db.Column(StringUUID, server_default=db.text('gen_random_uuid()'))
    app_id = db.Column(StringUUID, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    icon = db.Column(db.String(255))
    icon_background = db.Column(db.String(255))
    description = db.Column(db.Text)
    default_language = db.Column(db.String(255), nullable=False)
    copyright = db.Column(db.String(255))
    privacy_policy = db.Column(db.String(255))
    custom_disclaimer = db.Column(db.String(255), nullable=False)
    customize_domain = db.Column(db.String(255))
    customize_token_strategy = db.Column(db.String(255), nullable=False)
    prompt_public = db.Column(db.Boolean, nullable=False, server_default=db.text('false'))
    status = db.Column(db.String(255), nullable=False, server_default=db.text("'normal'::character varying"))
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    code = db.Column(db.String(255))

    @staticmethod
    def generate_code(n):
        while True:
            result = generate_string(n)
            while db.session.query(Site).filter(Site.code == result).count() > 0:
                result = generate_string(n)
            return result

    @property
    def app_base_url(self):
        return (
            current_app.config['APP_WEB_URL'] if current_app.config['APP_WEB_URL'] else request.host_url.rstrip('/'))
