from re import M
from typing import Union

# from tarfile import SUPPORTED_TYPES
from typing import Optional, List
from datetime import datetime
from .exceptions import (
    KeyNotCompatibleWithObjectException,
    KeyNotCompatibleException,
    IncompatibleObjectTypeException,
)
from .datastore.task_utils import init_datastorage_object


class MetaflowDataArtifactReference:

    _MODULE_IMPORTS = {}

    TYPE = None

    REQUIRED_FIELDS = {
        "url": str,
        "key": str,
        "pathspec": str,
        "attempt": int,
        "created_on": str,
        "type": str,
    }

    OPTIONAL_FIELDS = {
        "metadata": dict,
        "name": str,
        "size": int,
    }

    @property
    def size(self):
        return self._values.get("size", None)

    # PROPERTIES :
    @property
    def url(self):
        return self._values["url"]

    @property
    def key(self):
        return self._values["key"]

    @property
    def pathspec(self):
        return self._values.get("pathspec")

    @property
    def attempt(self):
        return self._values.get("attempt")

    @property
    def created_on(self):
        return self._values["created_on"]

    @property
    def metadata(self):
        return self._values.get("metadata")

    def __init__(self, **kwargs):
        self.validate(kwargs)
        self._values = kwargs

    def validate(self, data):
        for key, value in data.items():
            if key in self.REQUIRED_FIELDS and not isinstance(
                value, self.REQUIRED_FIELDS[key]
            ):
                raise ValueError(
                    f"Value {value} for key {key} not of type {self.REQUIRED_FIELDS[key]}"
                )

        misisng_keys = set(self.REQUIRED_FIELDS.keys()) - set(
            data.keys()
        )  # keys in schema but not in data
        if misisng_keys:
            # Missing keys for required fields is not fine
            raise ValueError(f"Missing keys {misisng_keys} for required fields")

        return True

    @classmethod
    def from_dict(cls, data) -> Union["ModelArtifact", "CheckpointArtifact"]:
        return Factory.from_dict(data)

    @classmethod
    def hydrate(
        cls,
        data: Union["ModelArtifact", "CheckpointArtifact", dict],
    ):
        if isinstance(data, dict):
            return cls.from_dict(data)
        return data

    def to_dict(self):
        values = self._values.copy()
        values["type"] = self.TYPE
        return values

    # ! INHERIT AND OVERRIDE (Private from user)
    def _load(self, storage_backend, local_path):
        raise NotImplementedError

    # ! INHERIT AND OVERRIDE (Private from user)
    @classmethod
    def _valid_reference_key(cls, reference_key):
        raise NotImplementedError

    @classmethod
    def _load_from_key(cls, key, local_path, storage_backend):
        raise NotImplementedError

    @classmethod
    def _load_metadata_from_key(cls, key, storage_backend):
        raise NotImplementedError


class ModelArtifact(MetaflowDataArtifactReference):

    OPTIONAL_FIELDS = {
        "metadata": dict,
        "serializer": Optional[str],
        "source": Optional[
            str
        ],  # Did it come from metaflow Task from something liked HF-HUB, etc.
        "lineage": Optional[List],
        "url": str,
        "key": str,
        "storage_format": str,
        "blob": bytes,  # bytes blob
        "label": str,
        "size": int,  # In bytes
    }

    REQUIRED_FIELDS = {
        "pathspec": str,
        "attempt": int,
        "created_on": str,
        "type": str,
        "model_uuid": str,
    }

    TYPE = "model"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def blob(self):
        return self._values.get("blob", None)

    @property
    def uuid(self):
        return self._values.get("model_uuid", None)

    @property
    def serializer(self):
        return self._values.get("serializer", None)

    @property
    def source(self):
        return self._values.get("source", None)

    @property
    def storage_format(self):
        return self._values.get("storage_format", None)

    @classmethod
    def create(
        cls,
        pathspec=None,
        attempt=None,
        key=None,
        url=None,
        model_uuid=None,
        metadata=None,
        storage_format=None,
        source=None,
        serializer=None,
        label=None,
    ):
        return cls(
            pathspec=pathspec,
            attempt=attempt,
            key=key,
            created_on=datetime.now().isoformat(),
            type=cls.TYPE,
            url=url,
            model_uuid=model_uuid,
            metadata=metadata,
            source=source,
            storage_format=storage_format,
            serializer=serializer,
            label=label,
        )

    def _set_blob(self, blob: bytes):
        self._values["blob"] = blob

    def _load(self, storage_backend, local_path):
        from .modeling_utils.core import _load_model

        _load_model(storage_backend, self.key, local_path)

    @classmethod
    def _valid_reference_key(cls, reference_key):
        from .modeling_utils.model_storage import ModelDatastore

        try:
            ModelDatastore.decompose_key(reference_key)
            return True
        except KeyNotCompatibleWithObjectException:
            return False

    @classmethod
    def _load_from_key(cls, key, local_path, storage_backend):
        from .modeling_utils.core import _load_model

        _load_model(storage_backend, model_key=key, path=local_path)

    @classmethod
    def _load_metadata_from_key(cls, key, storage_backend) -> "ModelArtifact":
        from .modeling_utils.core import _load_model_metadata

        return cls(
            **_load_model_metadata(
                storage_backend,
                model_key=key,
            )
        )


class CheckpointArtifact(MetaflowDataArtifactReference):

    TYPE = "checkpoint"

    REQUIRED_FIELDS = {
        "url": str,
        "key": str,
        "created_on": str,
        "type": str,
        # This means weather the checkpoint was created within Metaflow context or outside Metaflow context.
        # `creation_context` can be either `task` or `non-task`
    }

    OPTIONAL_FIELDS = {
        "creation_context": str,
        "pathspec": str,
        "attempt": int,
        "metadata": dict,
        "name": str,
        "version_id": str,
        "storage_format": str,
    }

    @property
    def storage_format(self):
        return self._values.get("storage_format", None)

    @property
    def version_id(self):
        return self._values.get("version_id", None)

    @property
    def name(self):
        return self._values.get("name")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _load(self, storage_backend, local_path):
        # TODO [POST RELEASE]: Check if we can move this somewhere else.
        # TODO : The connective tissue with checkpointer is not designed optimally.
        # Need to fix the design of checkpointer and constructors to figure
        # the best means of using the abstractions.
        from .checkpoints.core import Checkpointer

        _checkpointer = Checkpointer._from_checkpoint_and_storage_backend(
            self, storage_backend
        )
        _checkpointer._load_checkpoint(
            local_path=local_path,
            version_id=self.version_id,
            name=self.name,
            storage_format=self.storage_format,
        )

    @classmethod
    def _valid_reference_key(cls, reference_key):
        from .checkpoints.checkpoint_storage import CheckpointDatastore

        try:
            CheckpointDatastore.decompose_key(reference_key)
            return True
        except KeyNotCompatibleWithObjectException:
            return False

    @classmethod
    def _load_from_key(cls, key, local_path, storage_backend):
        from .checkpoints.constructors import load_checkpoint

        load_checkpoint(key, local_path)

    @classmethod
    def _load_metadata_from_key(cls, key, storage_backend):
        from .checkpoints.core import Checkpointer
        from .checkpoints.checkpoint_storage import CheckpointDatastore

        key_decomp = CheckpointDatastore.decompose_key(key)
        _checkpointer = Checkpointer._from_key(key)
        return cls(
            **_checkpointer.load_metadata(
                version_id=key_decomp.version_id,
                name=key_decomp.name,
            )
        )


class Factory:

    SUPPORTED_TYPES = [
        ModelArtifact.TYPE,
        CheckpointArtifact.TYPE,
    ]

    @classmethod
    def hydrate(cls, data):
        if isinstance(data, dict):
            return cls.from_dict(data)
        elif type(data) in [
            ModelArtifact,
            CheckpointArtifact,
        ]:
            return data
        else:
            raise ValueError("Data is not a dict or an instance of Artifact")

    @classmethod
    def from_dict(cls, data):
        if "type" not in data or data["type"] not in cls.SUPPORTED_TYPES:
            raise IncompatibleObjectTypeException(
                "Object type %s not in supported types: %s"
                % (data.get("type") or str(data), cls.SUPPORTED_TYPES)
            )
        if data["type"] == ModelArtifact.TYPE:
            return ModelArtifact(**data)
        if data["type"] == CheckpointArtifact.TYPE:
            return CheckpointArtifact(**data)

    @classmethod
    def load(cls, data, local_path, storage_backend):
        # `data` here is the dictionary/python object
        art = cls.hydrate(data)
        art._load(storage_backend, local_path)

    @classmethod
    def object_type_from_key(cls, reference_key):
        for obj_type in [ModelArtifact, CheckpointArtifact]:
            if obj_type._valid_reference_key(reference_key):
                return obj_type
        return None

    @classmethod
    def load_from_key(cls, key_object, local_path, storage_backend):
        obj_type = cls.object_type_from_key(key_object)
        if obj_type is None:
            raise KeyNotCompatibleException(
                key_object,
                supported_types=", ".join(
                    [ModelArtifact.TYPE, CheckpointArtifact.TYPE]
                ),
            )
        obj_type._load_from_key(key_object, local_path, storage_backend)

    @classmethod
    def load_metadata_from_key(
        cls, key_object, storage_backend
    ) -> Union[CheckpointArtifact, ModelArtifact]:
        obj_type = cls.object_type_from_key(key_object)
        if obj_type is None:
            raise KeyNotCompatibleException(
                key_object,
                supported_types=", ".join(
                    [ModelArtifact.TYPE, CheckpointArtifact.TYPE]
                ),
            )
        return obj_type._load_metadata_from_key(key_object, storage_backend)


def load_model(
    reference: Union[str, MetaflowDataArtifactReference, dict],
    path: str,
):
    """
    Load a model or checkpoint from Metaflow's datastore to a local path.

    This function provides a convenient way to load models and checkpoints that were previously saved using `@model`, `@checkpoint`, or `@huggingface_hub` decorators, either from within a Metaflow task or externally using the Run API.

    Parameters
    ----------
    reference : Union[str, MetaflowDataArtifactReference, dict]
        The reference to the model/checkpoint to load. This can be A string key (e.g., "model/my_model_abc123") OR A MetaflowDataArtifactReference object OR a dictionary artifact reference (e.g., self.my_model from a previous step)
    path : str
        The local filesystem path where the model/checkpoint should be loaded. The directory will be created if it doesn't exist.

    Raises
    ------
    ValueError
        If reference or path is None
    KeyNotCompatibleException
        If the reference key is not compatible with supported artifact types

    Examples
    --------
    **Loading within a Metaflow task:**

    ```python
    from metaflow import FlowSpec, step


    class MyFlow(FlowSpec):
        @model
        @step
        def train(self):
            # Save a model
            self.my_model = current.model.save(
                "/path/to/trained/model",
                label="trained_model"
            )
            self.next(self.evaluate)

        @step
        def evaluate(self):
            from metaflow import load_model
            # Load the model using the artifact reference
            load_model(self.my_model, "/tmp/loaded_model")
            # Model is now available at /tmp/loaded_model
            self.next(self.end)
    ```

    **Loading externally using Metaflow's Run API:**

    ```python
    from metaflow import Run
    from metaflow import load_model

    # Get a reference to a completed run
    run = Run("MyFlow/123")

    # Load using artifact reference from a step
    task_model_ref = run["train"].task.data.my_model
    load_model(task_model_ref, "/local/path/to/model")

    model_ref = run.data.my_model
    load_model(model_ref, "/local/path/to/model")
    ```

    **Loading HuggingFace models:**

    ```python
    # If you saved a HuggingFace model reference
    @huggingface_hub
    @step
    def download_hf_model(self):
        self.hf_model = current.huggingface_hub.snapshot_download(
            repo_id="mistralai/Mistral-7B-Instruct-v0.1"
        )
        self.next(self.use_model)

    @step
    def use_model(self):
        from metaflow import load_model
        # Load the HuggingFace model
        load_model(self.hf_model, "/tmp/mistral_model")
        # Model files are now available at /tmp/mistral_model
    ```
    """
    if reference is None:
        raise ValueError("`load_model` requires a reference")
    if path is None:
        raise ValueError("`load_model` requires a path to load the model")

    storage_backend = init_datastorage_object()
    if type(reference) == dict or isinstance(reference, MetaflowDataArtifactReference):
        Factory.load(
            Factory.hydrate(reference),
            path,
            storage_backend,
        )
    elif type(reference) == str:
        Factory.load_from_key(reference, path, storage_backend)


# We need this here because it will help ensure that stubs for the right packages get picked up
# Are adding it here because this seems to be one of the main entry points for stubs from the top level import of
# This module.
_addl_stubgen_modules = [
    "metaflow_extensions.obcheckpoint.plugins.machine_learning_utilities.checkpoints.decorator",
    "metaflow_extensions.obcheckpoint.plugins.machine_learning_utilities.hf_hub.decorator",
    "metaflow_extensions.obcheckpoint.plugins.machine_learning_utilities.modeling_utils.core",
]
