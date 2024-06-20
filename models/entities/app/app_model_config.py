import json

from extensions.ext_database import db
from models import StringUUID
from models.entities.app.app_annotation_setting import AppAnnotationSetting
from models.entities.app.app_entity import App


class AppModelConfig(db.Model):
    __tablename__ = 'app_model_configs'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='app_model_configs_pk'),
        db.Index('app_app_id_idx', 'app_id'),
    )
    id = db.Column(StringUUID, server_default=db.text('gen_random_uuid()'))
    app_id = db.Column(StringUUID, nullable=False)
    provider = db.Column(db.String(255), nullable=True)
    model_id = db.Column(db.String(255), nullable=True)
    configs = db.Column(db.JSON, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    opening_statement = db.Column(db.Text)
    suggested_question = db.Column(db.Text)
    suggested_question_after = db.Column(db.Text)
    speech_to_text = db.Column(db.Text)
    text_to_speech = db.Column(db.Text)
    more_like_this = db.Column(db.Text)
    model = db.Column(db.Text)
    user_input_form = db.Column(db.Text)
    dataset_query_variable = db.Column(db.String(255))
    pre_prompt = db.Column(db.Text)
    agent_mode = db.Column(db.Text)
    sensitive_word_avoidance = db.Column(db.Text)
    retriever_resource = db.Column(db.Text)
    prompt_type = db.Column(db.String(255), nullable=False, server_default=db.text("'simple'::character varying"))
    chat_prompt_config = db.Column(db.Text)
    completion_prompt_config = db.Column(db.Text)
    dataset_configs = db.Column(db.Text)
    external_data_tools = db.Column(db.Text)
    file_upload = db.Column(db.Text)

    @property
    def app(self):
        app = db.session.query(App).filter(App.id == self.app_id).first()
        return app

    @property
    def model_dict(self) -> dict:
        return json.loads(self.model) if self.model else None

    @property
    def suggested_questions_list(self) -> list:
        return json.loads(self.suggested_questions) if self.suggested_questions else []

    @property
    def suggested_questions_after_answer_dict(self) -> dict:
        return json.loads(self.suggested_questions_after_answer) if self.suggested_questions_after_answer \
            else {"enabled": False}

    @property
    def speech_to_text_dict(self) -> dict:
        return json.loads(self.speech_to_text) if self.speech_to_text \
            else {"enabled": False}

    @property
    def text_to_speech_dict(self) -> dict:
        return json.loads(self.text_to_speech) if self.text_to_speech \
            else {"enabled": False}

    @property
    def retriever_resource_dict(self) -> dict:
        return json.loads(self.retriever_resource) if self.retriever_resource \
            else {"enabled": False}

    @property
    def annotation_reply_dict(self) -> dict:
        annotation_setting = db.session.query(AppAnnotationSetting).filter(
            AppAnnotationSetting.app_id == self.app_id).first()
        if annotation_setting:
            collection_binding_detail = annotation_setting.collection_binding_detail
            return {
                "id": annotation_setting.id,
                "enabled": True,
                "score_threshold": annotation_setting.score_threshold,
                "embedding_model": {
                    "embedding_provider_name": collection_binding_detail.provider_name,
                    "embedding_model_name": collection_binding_detail.model_name
                }
            }

        else:
            return {"enabled": False}