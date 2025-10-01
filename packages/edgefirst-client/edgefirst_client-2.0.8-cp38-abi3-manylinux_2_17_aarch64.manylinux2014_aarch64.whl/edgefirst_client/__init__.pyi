from datetime import datetime
from enum import Enum
from pathlib import Path
from polars import DataFrame
from typing import Callable, Dict, Optional, List, Tuple, Union


Progress = Callable[[int, int], None]
ParameterValue = Union[str, float, bool]
Parameter = Union[ParameterValue,
                  List[ParameterValue],
                  Dict[str, ParameterValue]]


class Error(Exception):
    ...


class Dataset:  # pyright: ignore[reportRedeclaration]
    ...


class Client:  # pyright: ignore[reportRedeclaration]
    ...


class ID:
    """
    This is the ID class for EdgeFirst Studio.  Internally an ID is an unsigned
    64-bit integer.  Objects in Studio are represented with a type identifier
    followed by the ID in hex, for example experiments would be exp-a12 while
    a training session could be t-1f.  This class handles translating between
    the integer and string representations of IDs.
    """

    def __init__(self, id: int):
        """
        Create a new ID from the specified integer value.
        """
        ...

    def value(self) -> int:
        """
        Returns the integer value of the ID.
        """
        ...


class Organization:
    """
    The Organization class represents an organization in EdgeFirst Studio.
    An organization contains projects, users, and other resources related to
    a specific company or team.
    """
    @property
    def id(self) -> ID:
        """
        The unique identifier for the organization.
        """
        ...

    @property
    def name(self) -> str:
        """
        The name of the organization.
        """
        ...

    @property
    def credits(self) -> int:
        """
        The number of credits available to the organization.
        """
        ...


class Project:
    """
    The project class represents a project in the EdgeFirst Studio.  A project
    contains datasets, experiments, and other resources related to a specific
    task or workflow.
    """

    @property
    def id(self) -> ID:
        """
        The unique identifier for the project.
        """
        ...

    @property
    def uid(self) -> str:
        """
        The unique string identifier for the object.
        """
        ...

    @property
    def name(self) -> str:
        """
        The name of the project.
        """
        ...

    @property
    def description(self) -> str:
        """
        The description of the project.
        """
        ...

    def datasets(self,
                 client: Client,
                 name: Optional[str] = None) -> List[Dataset]:
        """
        List the datasets in the project.

        Args:
            client: The client to use for the request.
            name: The name of the dataset to filter by.

        Returns:
            A list of datasets in the project.
        """
        ...


class AnnotationSet:
    """
    The AnnotationSet class represents the collection of annotations for a
    given dataset.  A dataset can have multiple annotation sets, each
    containing annotations for different tasks or purposes.
    """

    @property
    def id(self) -> ID:
        """The ID of the annotation set."""
        ...

    @property
    def uid(self) -> str:
        """
        The unique string identifier for the object.
        """
        ...

    @property
    def dataset_id(self) -> ID:
        """The ID of the dataset that the annotation set belongs to."""
        ...

    @property
    def name(self) -> str:
        """The name of the annotation set."""
        ...

    @property
    def description(self) -> str:
        """The description of the annotation set."""
        ...

    @property
    def created(self) -> datetime:
        """The creation date of the annotation set."""
        ...


class Label:
    """
    Representation of a label in EdgeFirst Studio.  Labels are used to identify
    annotations in a dataset.
    """

    @property
    def id(self) -> int:
        """The ID of the label."""
        ...

    @property
    def uid(self) -> str:
        """
        The unique string identifier for the object.
        """
        ...

    @property
    def name(self) -> str:
        """The name of the label."""
        ...

    @property
    def index(self) -> int:
        """The index of the label."""
        ...

    @property
    def dataset_id(self) -> ID:
        """The ID of the dataset that the label belongs to."""
        ...

    def remove(self, client: Client) -> None:
        """Remove the label from the dataset."""
        ...

    def set_name(self, client: Client, name: str) -> None:
        """Set the name of the label."""
        ...

    def set_index(self, client: Client, index: int) -> None:
        """Set the index of the label."""
        ...


class Dataset:
    """
    The dataset class represents a dataset in EdgeFirst Studio.  A dataset
    is a collection of sensor data such as images, lidar, radar along with
    annotations for bounding boxes, masks, or 3d bounding boxes.
    """

    @property
    def id(self) -> ID:
        """The ID of the dataset."""
        ...

    @property
    def uid(self) -> str:
        """
        The unique string identifier for the object.
        """
        ...

    @property
    def name(self) -> str:
        """The name of the dataset."""
        ...

    @property
    def description(self) -> str:
        """The description of the dataset."""
        ...

    @property
    def created(self) -> datetime:
        """The creation date of the dataset."""
        ...

    def labels(self, client: Client) -> List[Label]:
        """The labels associated with the dataset."""
        ...

    def add_label(self, client: Client, name: str) -> None:
        """Add a label to the dataset."""
        ...

    def remove_label(self, client: Client, name: str) -> None:
        """Remove a label from the dataset."""
        ...


class FileType(Enum):
    """
    The FileType represents the type of file used in the EdgeFirst client.

    Members:
        Image:
            A file with extension `.image.jpeg` that stores the image.
        LidarPcd:
            A file with extension `.lidar.pcd` that stores [x, y, z]
            Cartesian coordinates from the LiDAR sensor.
        LidarDepth:
            A file with extension `.lidar.png` that stores per-pixel
            depth values captured by the LiDAR sensor.
        LidarReflect:
            A file with extension `.lidar.jpeg` that stores reflectance data
            from the LiDAR sensor.
        RadarPcd:
            A file with extension `.radar.pcd` that stores [x, y, z] Cartesian
            coordinates in meters from the Radar sensor, along with speed m/s,
            power, noise, and radar cross-section (RCS).
        RadarCube:
            A file with extension `.radar.png` that stores a range-doppler
            radar cube. The cube has dimensions: sequence, rx_antenna,
            range_bins, doppler_bins — encoded in a 16-bit PNG.
    """
    Image: "FileType"
    LidarPcd: "FileType"
    LidarDepth: "FileType"
    LidarReflect: "FileType"
    RadarPcd: "FileType"
    RadarCube: "FileType"


class AnnotationType(Enum):
    """
    The AnnotationType represents the type
    of annotation used in the Edgefirst client.

    Members:
        Box2d: 2D bounding box annotation.
        Box3d: 3D bounding box annotation.
        Mask:  Pixel-wise segmentation mask.
    """
    Box2d: "AnnotationType"
    Box3d: "AnnotationType"
    Mask: "AnnotationType"


class Box2d:
    """
    The Box2d is a representation of a single 2D bounding box annotation
    which is a pixel-based annotation for the image that is stored in
    EdgeFirst Datasets.  The bounding boxes are normalized to the image
    dimensions (float32 values between 0 and 1).  The width and height of the
    box are provided through the `width` and `height` properties while the
    position of the box can be represented in two ways: either through the
    `left` and `top` properties which represent the top-left corner of
    the box or through the `cx` and `cy` properties which represent the
    center of the box.
    """

    def __init__(self,
                 left: float,
                 top: float,
                 width: float,
                 height: float) -> None:
        """
        Create a new bounding box representation given the coordinates
        [xc, yc, width, height] or [xmin, ymin, width, height] of the
        bounding box.  The coordinates should be normalized to
        the image dimensions.

        Args:
            x (float): The normalized x-center or xmin coordinate
                       of the bounding box.
            y (float): The normalized y-center or ymin coordinate
                       of the bounding box.
            width (float): The normalized width of the bounding box.
            height (float): The normalized height of the bounding box.
        """
        ...

    @property
    def width(self) -> float:
        """
        Returns the width of the bounding box.  This dimension is normalized
        to the image width.

        Returns:
            float: The width of the bounding box.
        """
        ...

    @property
    def height(self) -> float:
        """
        Returns the height of the bounding box.  This dimension is normalized
        to the image height.

        Returns:
            float: The height of the bounding box.
        """
        ...

    @property
    def left(self) -> float:
        """
        Returns the left coordinate of the bounding box.  This is either
        the x-center or xmin coordinate of the bounding box.

        Returns:
            float: The left coordinate of the bounding box.
        """
        ...

    @property
    def top(self) -> float:
        """
        Returns the y-coordinate of the bounding box.  This is either
        the y-center or ymin coordinate of the bounding box.

        Returns:
            float: The y-coordinate of the bounding box.
        """
        ...

    @property
    def cx(self) -> float:
        """
        Returns the x-center coordinate of the bounding box.  This coordinate
        is normalized to the image width.

        Returns:
            float: The x-center coordinate of the bounding box.
        """
        ...

    @property
    def cy(self) -> float:
        """
        Returns the y-center coordinate of the bounding box.  This coordinate
        is normalized to the image height.

        Returns:
            float: The y-center coordinate of the bounding box.
        """
        ...


class Box3d:
    """
    The Box3d is a representation of a single 3D bounding box annotation
    which is based in meters.  The bounding boxes are float32 values containing
    the fields [x, y, z, width, height, depth].  This follows the convention
    for the Sensor Coordinate Frame where the x-axis is forward, y-axis is
    left, and z-axis is up.
    """

    def __init__(self,
                 cx: float,
                 cy: float,
                 cz: float,
                 width: float,
                 height: float,
                 depth: float) -> None:
        """
        Initialize a 3D bounding box with the given position and dimensions.

        Args:
            cx (float): The x-coordinate of the box center (forward).
            cy (float): The y-coordinate of the box center (left).
            cz (float): The z-coordinate of the box center (up).
            width (float): The width of the box along the y-axis.
            height (float): The height of the box along the z-axis.
            depth (float): The depth of the box along the x-axis.
        """
        ...

    @property
    def width(self) -> float:
        """
        The width of the bounding box along the y-axis.

        Returns:
            float: The width in meters.
        """
        ...

    @property
    def height(self) -> float:
        """
        The height of the bounding box along the z-axis.

        Returns:
            float: The height in meters.
        """
        ...

    @property
    def length(self) -> float:
        """
        The length of the bounding box along the x-axis.

        Returns:
            float: The length in meters.
        """
        ...

    @property
    def cx(self) -> float:
        """
        The x-coordinate of the box center (forward direction).

        Returns:
            float: The x-coordinate in meters.
        """
        ...

    @property
    def cy(self) -> float:
        """
        The y-coordinate of the box center (left direction).

        Returns:
            float: The y-coordinate in meters.
        """
        ...

    @property
    def cz(self) -> float:
        """
        The z-coordinate of the box center (up direction).

        Returns:
            float: The z-coordinate in meters.
        """
        ...

    @property
    def left(self) -> float:
        """
        The left coordinate of the bounding box along the y-axis.

        Returns:
            float: The left coordinate in meters.
        """
        ...

    @property
    def top(self) -> float:
        """
        The top coordinate of the bounding box along the z-axis.

        Returns:
            float: The top coordinate in meters.
        """
        ...

    @property
    def front(self) -> float:
        """
        The front coordinate of the bounding box along the x-axis.

        Returns:
            float: The front coordinate in meters.
        """
        ...


class Mask:
    """
    Represents a segmentation mask using polygonal annotations.

    The mask is defined by one or more polygons, where each polygon is
    a list of [x, y] coordinates normalized to the image dimensions.
    All coordinates are float32 values between 0 and 1.
    """

    def __init__(self, polygon: List[List[float]]) -> None:
        """
        Initializes a new Mask instance from a list of polygons.

        Args:
            polygon (List[List[float]]): A list of polygons, where each polygon
                                         is a list of [x, y] float coordinates
                                         normalized to the image dimensions.
        """
        ...

    @property
    def polygon(self) -> List[List[float]]:
        """
        Returns the polygon data defining the mask.

        Each polygon is a list of [x, y] coordinates, with values
        normalized to the image dimensions.

        Returns:
            List[List[float]]: A list of polygons representing the mask.
        """
        ...


class Annotation:
    """
    Represents a single annotation associated
    with a sample in an EdgeFirst dataset.

    An annotation may include sensor metadata such as
    (name, group, label, etc.) as well as 2D/3D bounding boxes
    and segmentation masks.
    """

    @property
    def sample_id(self) -> Optional[ID]:
        """
        The ID of the sample this annotation belongs to.

        Returns:
            Optional[ID]: The sample ID, or None if not available.
        """
        ...

    @property
    def name(self) -> Optional[str]:
        """
        The name of the annotation instance, if specified.  The name
        is derived from device hostname and the date and time and the
        specific frame from the recording "hostname_date_time_frame".

        Returns:
            Optional[str]: The instance name or None.
        """
        ...

    @property
    def group(self) -> Optional[str]:
        """
        The group this annotation belongs to, if specified.  A group
        can be "train", "val", etc.

        Returns:
            Optional[str]: The group name or None.
        """
        ...

    @property
    def sequence_name(self) -> Optional[str]:
        """
        The sequence name this annotation is part of, if any.  The sequence
        name is derived from the device hostname and the date and time
        of the recording hostname_date_time.

        Returns:
            Optional[str]: The sequence name or None.
        """
        ...

    @property
    def object_id(self) -> Optional[str]:
        """
        A unique identifier for the object associated with this annotation.

        Returns:
            Optional[str]: The object ID or None.
        """
        ...

    @property
    def label(self) -> Optional[str]:
        """
        The semantic label (e.g., "car", "pedestrian") for this annotation.

        Returns:
            Optional[str]: The label or None.
        """
        ...

    @property
    def label_index(self) -> Optional[int]:
        """
        The index of the label for this annotation.

        Returns:
            Optional[int]: The label index or None.
        """
        ...

    @property
    def box2d(self) -> Optional[Box2d]:
        """
        The 2D bounding box associated with this annotation, if available.

        Returns:
            Optional[Box2d]: The 2D bounding box or None.
        """
        ...

    @property
    def box3d(self) -> Optional[Box3d]:
        """
        The 3D bounding box associated with this annotation, if available.

        Returns:
            Optional[Box3d]: The 3D bounding box or None.
        """
        ...

    @property
    def mask(self) -> Optional[Mask]:
        """
        The segmentation mask associated with this annotation, if available.

        Returns:
            Optional[Mask]: The segmentation mask or None.
        """
        ...


class Sample:
    """
    Represents a single data sample in the EdgeFirst dataset.
    A sample includes metadata and associated annotations, and
    can be used to download file content for different sensor modalities.
    """

    @property
    def id(self) -> ID:
        """
        Returns the unique identifier of the sample.

        Returns:
            ID: The sample ID.
        """
        ...

    @property
    def uid(self) -> str:
        """
        The unique string identifier for the object.
        """
        ...

    @property
    def name(self) -> str:
        """
        Returns the name of the sample.

        Returns:
            str: The sample name.
        """
        ...

    @property
    def group(self) -> Optional[str]:
        """
        Returns the group name of the sample, if any.

        Returns:
            Optional[str]: The group name or None.
        """
        ...

    @property
    def sequence_name(self) -> Optional[str]:
        """
        Returns the sequence name to which this sample belongs, if any.

        Returns:
            Optional[str]: The sequence name or None.
        """
        ...

    @property
    def annotations(self) -> List[Annotation]:
        """
        Returns the list of annotations associated with this sample.

        Returns:
            List[Annotation]: A list of annotation objects.
        """
        ...

    def download(self, client: Client,
                 file_type: FileType = FileType.Image) -> Optional[bytes]:
        """
        Downloads the data file for this sample using the given file type.

        Args:
            client (Client): The client instance used to download the file.
            file_type (FileType, optional): The type of file to download.
                                            Defaults to FileType.Image.

        Returns:
            Optional[bytes]: The raw file data as bytes,
                             or None if no file exists.
        """
        ...


class Experiment:
    """
    Represents an experiment in EdgeFirst Studio which are used to organize
    training and validation sessions.
    """

    @property
    def id(self) -> ID:
        """
        Returns the unique identifier of the experiment.

        Returns:
            ID: The experiment ID.
        """
        ...

    @property
    def uid(self) -> str:
        """
        The unique string identifier for the object.
        """
        ...

    @property
    def name(self) -> str:
        """
        Returns the name of the experiment.

        Returns:
            str: The experiment name.
        """
        ...

    @property
    def description(self) -> Optional[str]:
        """
        Returns the description of the experiment, if any.

        Returns:
            Optional[str]: The experiment description or None.
        """
        ...


class Task:
    """
    Represents an EdgeFirst Studio Cloud Task.  A task could be a docker
    instance or an EC2 instance or similar.
    """

    @property
    def id(self) -> ID:
        """
        Returns the unique identifier of the Docker task.

        Returns:
            ID: The Docker task ID.
        """
        ...

    @property
    def uid(self) -> str:
        """
        The unique string identifier for the object.
        """
        ...

    @property
    def name(self) -> str:
        """
        Returns the name of the Docker task.

        Returns:
            str: The Docker task name.
        """
        ...

    @property
    def status(self) -> str:
        """
        Returns the status of the Docker task.

        Returns:
            str: The Docker task status.
        """
        ...

    @property
    def workflow(self) -> str:
        """
        Returns the task workflow which could be trainer or validation 
        workflows.

        Returns:
            str: The task workflow.
        """
        ...

    @property
    def manager(self) -> str:
        """
        Returns the manager type for the task.  The manager could be cloud,
        user, or kubernetes.

        Returns:
            str: The task manager type.
        """
        ...

    @property
    def instance(self) -> str:
        """
        Returns the instance type for the task.  The instance type depends on
        the manager, for cloud manager it is the AWS EC2 instance type.

        Returns:
            str: The task instance type.
        """
        ...

    @property
    def created(self) -> datetime:
        """
        Returns the creation date of the Docker task.

        Returns:
            datetime: The Docker task creation date.
        """
        ...


class Stage:
    """
    Represents a stage in the task.
    """

    @property
    def task_id(self) -> ID:
        """
        Returns the ID of the task associated with this stage.

        Returns:
            ID: The task ID.
        """
        ...

    @property
    def stage_id(self) -> ID:
        """
        Returns the ID of the stage.

        Returns:
            ID: The stage ID.
        """
        ...

    @property
    def status(self) -> Optional[str]:
        """
        Returns the status of the stage.

        Returns:
            str: The stage status.
        """
        ...

    @property
    def description(self) -> Optional[str]:
        """
        Returns the description of the stage, if any.

        Returns:
            Optional[str]: The stage description or None.
        """
        ...

    @property
    def message(self) -> Optional[str]:
        """
        Returns the message associated with the stage, if any.

        Returns:
            Optional[str]: The stage message or None.
        """
        ...

    @property
    def percentage(self) -> int:
        """
        Returns the completion percentage of the stage.

        Returns:
            int: The stage completion percentage as an integer, each step
                 representing 1% of the total.
        """
        ...


class TaskInfo:
    """
    The TaskInfo class provides detailed information about a specific task such
    as its status and progress.
    """

    @property
    def id(self) -> ID:
        """
        Returns the unique identifier of the task.

        Returns:
            ID: The task ID.
        """
        ...

    @property
    def uid(self) -> str:
        """
        Returns the unique string identifier for the task.

        Returns:
            str: The task UID.
        """
        ...

    @property
    def project_id(self) -> ID:
        """
        Returns the ID of the project associated with the task.

        Returns:
            ID: The project ID.
        """
        ...

    @property
    def description(self) -> str:
        """
        Returns the description of the task, if any.

        Returns:
            Optional[str]: The task description or None.
        """
        ...

    @property
    def status(self) -> str:
        """
        Returns the status of the task.

        Returns:
            str: The task status.
        """
        ...

    @property
    def stages(self) -> Dict[str, Stage]:
        """
        Returns the stages of the task.

        Returns:
            Dict[str, Stage]: A dictionary of stage names to Stage objects.
        """
        ...

    @property
    def created(self) -> datetime:
        """
        Returns the creation date of the task.

        Returns:
            datetime: The task creation date.
        """
        ...

    @property
    def completed(self) -> datetime:
        """
        Returns the completion date of the task, if any.

        Returns:
            datetime: The task completion date or None.
        """
        ...

    def set_status(self, client: Client, status: str) -> None:
        """
        Sets the status of the task.

        Args:
            client (Client): The EdgeFirst client.
            status (str): The new status for the task.
        """
        ...

    def set_stages(self,
                   client: Client,
                   stages: List[Tuple[str, str]]) -> None:
        """
        Sets the stages of the task.

        Args:
            client (Client): The EdgeFirst client.
            stages (List[Tuple[str, str]]): A list of tuples containing stage
                                            names and descriptions.
        """

    def update_stage(self,
                     client: Client,
                     stage_name: str,
                     status: Optional[str] = None,
                     message: Optional[str] = None,
                     percentage: Optional[int] = None) -> None:
        """
        Updates a specific stage of the task.

        Args:
            client (Client): The EdgeFirst client.
            stage_name (str): The name of the stage to update.
            status (Optional[str]): The new status for the stage.
            message (Optional[str]): A message associated with the stage.
            percentage (Optional[int]): The completion percentage of the stage.
        """
        ...


class DatasetParams:
    """
    Represents the parameters for a dataset used in a training session.
    """

    @property
    def dataset_id(self) -> ID:
        """
        Returns the ID of the dataset associated with these parameters.

        Returns:
            ID: The dataset ID.
        """
        ...

    @property
    def annotation_set_id(self) -> ID:
        """
        Returns the ID of the annotation set associated with these parameters.

        Returns:
            ID: The annotation set ID.
        """
        ...

    @property
    def train_group(self) -> str:
        """
        Returns the name of the selected training group.

        Returns:
            str: The training group name.
        """
        ...

    @property
    def val_group(self) -> str:
        """
        Returns the name of the selected validation group.

        Returns:
            str: The validation group name.
        """
        ...


class Artifact:
    """
    Represents an artifact produced by a training session.
    """

    @property
    def name(self) -> str:
        """
        Returns the name of the artifact.

        Returns:
            str: The artifact name.
        """
        ...

    @property
    def model_type(self) -> str:
        """
        Returns the type of the model used in the artifact.

        Returns:
            str: The model type.
        """
        ...


class TrainingSession:
    """
    A training session for a specific experiment, this represents the
    configuration and state of the training process.
    """

    @property
    def id(self) -> ID:
        """
        Returns the unique identifier of the training session.

        Returns:
            ID: The training session ID.
        """
        ...

    @property
    def uid(self) -> str:
        """
        The unique string identifier for the object.
        """
        ...

    @property
    def experiment_id(self) -> ID:
        """
        Returns the ID of the experiment associated with this training session.

        Returns:
            ID: The experiment ID.
        """
        ...

    @property
    def name(self) -> str:
        """
        Returns the name of the training session.

        Returns:
            str: The training session name.
        """
        ...

    @property
    def description(self) -> Optional[str]:
        """
        Returns the description of the training session, if any.

        Returns:
            Optional[str]: The training session description or None.
        """
        ...

    @property
    def model(self) -> str:
        """
        Returns the model used in the training session.

        Returns:
            str: The model implementation name.
        """
        ...

    @property
    def task(self) -> Task:
        """
        Returns the Docker task associated with the training session.

        Returns:
            Task: The Docker task object.
        """
        ...

    @property
    def model_params(self) -> Dict[str, Parameter]:
        """
        Returns the model parameters used in the training session.

        Returns:
            Dict[str, Parameter]: The model parameters.
        """
        ...

    @property
    def dataset_params(self) -> DatasetParams:
        """
        Returns the dataset parameters used in the training session.

        Returns:
            DatasetParams: The dataset parameters object.
        """
        ...

    def metrics(self, client: Client) -> Dict[str, Parameter]:
        """
        Returns the metrics associated with the training session.

        Args:
            client (Client): The EdgeFirst client.

        Returns:
            Dict[str, Parameter]: The training session metrics.
        """
        ...

    def set_metrics(self,
                    client: Client,
                    metrics: Dict[str, Parameter]) -> None:
        """
        Sets the metrics for the training session.

        Args:
            client (Client): The EdgeFirst client.
            metrics (Dict[str, Parameter]): The training session metrics.
        """
        ...

    def artifacts(self, client: Client) -> List[Artifact]:
        """
        Returns a list of artifacts produced by the training session.

        Args:
            client (Client): The EdgeFirst client.

        Returns:
            List[Artifact]: A list of artifacts.
        """
        ...

    def upload_artifact(self,
                        client: Client,
                        filename: str,
                        path: Optional[Path] = None) -> None:
        """
        Uploads an artifact file to the training session.

        Args:
            client (Client): The EdgeFirst client.
            filename (str): The name of the artifact file.
            path (Optional[Path]): The local path to the artifact file.  If not
                                   specified the filename is used as the path.
        """
        ...

    def download_artifact(self, client: Client, filename: str) -> bytes:
        """
        Downloads the specified artifact file from the training session.  Note
        that to download with progress to an output file you can use the
        `client.download_artifact` method instead.

        Args:
            client (Client): The EdgeFirst client.
            filename (str): The name of the artifact file to download.

        Returns:
            bytes: The raw file data as bytes.
        """
        ...

    def upload_checkpoint(self,
                          client: Client,
                          filename: str,
                          path: Optional[Path] = None) -> None:
        """
        Uploads a checkpoint file to the training session.

        Args:
            client (Client): The EdgeFirst client.
            filename (str): The name of the checkpoint file.
            path (Optional[Path]): The local path to the checkpoint file. If
                                   not specified the filename is used as the
                                   path.
        """
        ...

    def download_checkpoint(self, client: Client, filename: str) -> bytes:
        """
        Downloads the specified checkpoint file from the training session.
        Note that to download with progress to an output file you can use the
        `client.download_artifact` method instead.

        Args:
            client (Client): The EdgeFirst client.
            filename (str): The filename for the checkpoint file to download.

        Returns:
            bytes: The raw file data as bytes.
        """
        ...

    def upload(self, client: Client, files: List[Tuple[str, Path]]) -> None:
        """
        Uploads files to the training session.  This can be used to upload
        model weights or other files that are needed for the training session.

        The first element in the files tuple is the target name for the file
        while the second element is the local path to the file.  The target
        name is the path where the file will be stored in the training session.

        Artifacts must be uploaded to `artifacts/*`, checkpoints to
        `checkpoints/*`,  while metrics should be uploaded to `metrics/*`.

        Args:
            client (Client): The EdgeFirst client.
            files (List[Tuple[str, Path]]): A list of tuples containing the
                                            target filename and the path to the
                                            file to upload.
        """
        ...

    def download(self, client: Client, filename: str) -> str:
        """
        Downloads the specified file from the training session.  This function
        requires the target file to only contain valid utf-8 as it is returned
        through a JSON response.  To retrieve binary files use the
        `client.download_artifact` method instead.

        Args:
            client (Client): The EdgeFirst client.
            filename (str): The name of the file to download.

        Returns:
            str: The raw file data as a string.
        """
        ...


class ValidationSession:
    """
    This class represents a validation session for a given model and dataset.
    """

    @property
    def id(self) -> ID:
        """
        Returns the unique identifier of the validation session.

        Returns:
            ID: The validation session ID.
        """
        ...

    @property
    def uid(self) -> str:
        """
        Returns the unique string identifier of the validation session.

        Returns:
            str: The validation session UID.
        """
        ...

    @property
    def name(self) -> str:
        """
        Returns the name of the validation session.

        Returns:
            str: The validation session name.
        """
        ...

    @property
    def description(self) -> str:
        """
        Returns the description of the validation session, if any.

        Returns:
            str: The validation session description or an empty string.
        """
        ...

    @property
    def dataset_id(self) -> ID:
        """
        Returns the ID of the dataset associated with this validation session.

        Returns:
            ID: The dataset ID.
        """
        ...

    @property
    def experiment_id(self) -> ID:
        """
        Returns the ID of the experiment associated with this validation
        session.

        Returns:
            ID: The experiment ID.
        """
        ...

    @property
    def training_session_id(self) -> ID:
        """
        Returns the ID of the training session associated with this validation
        session.

        Returns:
            ID: The training session ID.
        """
        ...

    @property
    def annotation_set_id(self) -> ID:
        """
        Returns the ID of the annotation set associated with this validation
        session.

        Returns:
            ID: The annotation set ID.
        """
        ...

    @property
    def params(self) -> Dict[str, Parameter]:
        """
        Returns the parameters associated with this validation session.

        Returns:
            Dict[str, Parameter]: The validation session parameters.
        """
        ...

    @property
    def task(self) -> Task:
        """
        Returns the Docker task associated with the validation session.

        Returns:
            Task: The Docker task object.
        """
        ...

    def metrics(self, client: Client) -> Dict[str, Parameter]:
        """
        Returns the metrics associated with the validation session.

        Args:
            client (Client): The EdgeFirst client.

        Returns:
            Dict[str, Parameter]: The validation session metrics.
        """
        ...

    def set_metrics(self, client: Client, metrics: Dict[str, Parameter]):
        """
        Sets the metrics for the validation session.

        Args:
            client (Client): The EdgeFirst client.
            metrics (Dict[str, Parameter]): The metrics to set.
        """
        ...

    def artifacts(self, client: Client) -> List[Artifact]:
        """
        Returns a list of artifacts produced by the validation session.

        Args:
            client (Client): The EdgeFirst client.

        Returns:
            List[Artifact]: A list of artifacts.
        """
        ...

    def upload(self, client: Client, files: List[Tuple[str, Path]]):
        """
        Uploads the specified files to the validation session.

        Args:
            client (Client): The EdgeFirst client.
            files (List[Tuple[str, Path]]): A list of tuples containing the
                                              target filename and the path to
                                              the file to upload.
        """
        ...


class Client:
    """
    The EdgeFirst Client handles the connection to the EdgeFirst Studio Server
    and manages authentication and the client RPC calls.  The client also
    provides various utility methods for interacting with datasets and
    converting them to and from Polars DataFrames.
    """

    def __init__(self,
                 token: Optional[str] = None,
                 username: Optional[str] = None,
                 password: Optional[str] = None,
                 server: Optional[str] = None,
                 use_token_file: bool = True) -> None:
        """
        Create a new EdgeFirst client instance.  The client has a few options
        for authentication.  A token can be provided directly to the client
        which is used to authenticate the client with the server and includes
        the server instance information.  Alternatively, a username and
        password can be provided to the client along with an optional server
        otherwise the default of "saas" is used.  If none of these options are
        provided the client will use the local user's configuration file to
        read the last saved token unless the `use_token_file` parameter is set
        to false.

        Args:
            token (Optional[str]): The authentication token for the client.
                                   If provided, this is used to authenticate
                                   the client with the server.
            username (Optional[str]): The username to log in to Studio.
            password (Optional[str]): The password to log in to Studio.
            server (Optional[str]): The server to connect to.  If not provided,
                                    the default server "saas" is used.
            use_token_file (bool): Whether to use the local token file for
                                   authentication if no token, username, or
                                   password is provided.  Defaults to true.
        """
        ...

    def version(self) -> str:
        """
        Return the version of the EdgeFirst Studio server for the current
        client connection.

        Returns:
            str: The version of the server.
        """
        ...

    def token(self) -> str:
        """
        Return the token used to authenticate the client with the server.  When
        logging into the server using a username and password, the token is
        returned by the server and stored in the client for future
        interactions.

        Returns:
            str: The token used to authenticate the client with the server.
        """
        ...

    def verify_token(self):
        """
        Verify the token used to authenticate the client with the server.  This
        method is used to ensure that the token is still valid and has not
        expired.  If the token is invalid, the server will return an error and
        the client will need to login again.

        Raises:
            Error: If the token is invalid or expired.
        """
        ...

    def renew_token(self):
        """
        Renew the token used to authenticate the client with the server.  This
        method is used to extend the expiration time of the token.  If the
        token is invalid or expired, the server will return an error and the
        client will need to login again.

        Raises:
            Error: If the token is invalid or expired.
        """
        ...

    @property
    def token_expiration(self) -> datetime:
        """
        Return the expiration date of the token used to authenticate the
        client with the server.

        Returns:
            datetime: The expiration date of the token.
        """
        ...

    def login(self, username: str, password: str):
        """
        Login to the server using the specified username and password.  The
        server will authenticate the user and return a token that can be used
        to authenticate future requests.  The token is stored in the client and
        used to authenticate the client with the server.

        Args:
            username (str): The username to log in to EdgeFirst Studio.
            password (str): The password to log in to EdgeFirst Studio.

        Raises:
            Error: If authentication fails.
        """
        ...

    @property
    def username(self) -> str:
        """
        Return the username associated with the current client.

        Returns:
            str: The username associated with the current client.

        Raises:
            Error: If the username cannot be accessed.
        """
        ...

    @property
    def server(self) -> str:
        """
        Return the server name associated with the current client.

        Returns:
            str: The server name associated with the current client.
        """
        ...

    def organization(self) -> Organization:
        """
        Return the organization associated with the current user.  The
        organization is the top-level entity in EdgeFirst Studio and contains
        projects, datasets, trainers, and trainer sessions.

        Returns:
            Organization: The organization associated with the current user.

        Raises:
            Error: If the organization cannot be accessed.
        """
        ...

    def projects(self, name: Optional[str] = None) -> List[Project]:
        """
        Returns a list of projects available to the user.  The projects are
        returned as a vector of Project objects.  If the name parameter is
        provided, only projects containing the specified name will be returned.

        Projects are the top-level organizational unit in EdgeFirst Studio.
        Projects contain datasets, trainers, and trainer sessions.  Projects
        are used to group related datasets and trainers together.

        Args:
            name (Optional[str]): The name of the project to filter by.

        Returns:
            List[Project]: A list of accessible projects.
        """
        ...

    def project(self, project_id: Union[ID, str]) -> Project:
        """
        Return the project with the specified project ID.  If the project does
        not exist, an error is returned.

        Args:
            project_id (Union[ID, str]): The ID of the project to retrieve.

        Returns:
            Project: The requested project.

        Raises:
            Error: If the project does not exist or cannot be accessed.
        """
        ...

    def datasets(self,
                 project_id: Union[ID, str],
                 name: Optional[str] = None) -> List[Dataset]:
        """
        Returns a list of datasets available to the user.  The datasets are
        returned as a vector of Dataset objects.  If a name is provided, only
        datasets with that name are returned.

        Args:
            project_id (Union[ID, str]): The project ID whose datasets to get.
            name (Optional[str]): The name of the dataset to filter by.

        Returns:
            List[Dataset]: A list of datasets.
        """
        ...

    def dataset(self, dataset_id: Union[ID, str]) -> Dataset:
        """
        Return the dataset with the specified dataset ID.  If the dataset does
        not exist, an error is returned.

        Args:
            dataset_id (Union[ID, str]): The ID of the dataset.

        Returns:
            Dataset: The requested dataset.

        Raises:
            Error: If the dataset does not exist or cannot be accessed.
        """
        ...

    def labels(self,
               client: Client,
               dataset_id: Union[ID, str]) -> List[Label]:
        """Get the labels associated with the dataset."""
        ...

    def add_label(self,
                  client: Client,
                  dataset_id: Union[ID, str],
                  name: str) -> None:
        """Add a label to the dataset."""
        ...

    def remove_label(self, client: Client, label_id: int) -> None:
        """Remove a label from the dataset."""
        ...

    def download_dataset(
        self,
        dataset_id: Union[ID, str],
        groups: List[str] = [],
        types: List[FileType] = [],
        output: Optional[str] = None,
        progress: Optional[Progress] = None
    ):
        """
        Download dataset samples matching specified groups and file types.

        Args:
            dataset_id (Union[ID, str]): ID of the dataset.
            groups (List[str]): Dataset groups to include (train, val, etc).
            types (List[FileType]): File types to download.
            output (str): Output directory to save downloaded files.
            progress (Optional[Progress]): Optional progress reporter.
        """
        ...

    def annotation_sets(self,
                        dataset_id: Union[ID, str]) -> List[AnnotationSet]:
        """
        Retrieve the annotation sets associated with the specified dataset.

        Args:
            dataset_id (Union[ID, str]): Dataset ID.

        Returns:
            List[AnnotationSet]: Annotation sets associated with the dataset.
        """
        ...

    def annotation_set(self,
                       annotation_set_id: Union[ID, str]) -> AnnotationSet:
        """
        Retrieve the annotation set with the specified ID.

        Args:
            annotation_set_id (Union[ID, str]): Annotation set ID.

        Returns:
            AnnotationSet: The requested annotation set.
        """
        ...

    def annotations(
        self,
        annotation_set_id: Union[ID, str],
        groups: List[str] = [],
        annotation_types: List[AnnotationType] = [],
        progress: Optional[Progress] = None
    ) -> List[Annotation]:
        """
        Get the annotations for the specified annotation set with the
        requested annotation types.  The annotation types are used to filter
        the annotations returned.  The groups parameter is used to filter for
        dataset groups (train, val, test).  Images which do not have any
        annotations are also included in the result as long as they are in the
        requested groups (when specified).

        The result is a vector of Annotations objects which contain the
        full dataset along with the annotations for the specified types.

        To get the annotations as a DataFrame, use the `annotations_dataframe`
        method instead.

        Args:
            annotation_set_id (Union[ID, str]): The ID of the annotation set.
            groups (List[str]): Dataset groups to include.
            annotation_types (List[AnnotationType]): Types of annotations
                                                     to include.
            progress (Optional[Progress]): Optional progress reporter.

        Returns:
            List[Annotation]: List of annotations.
        """
        ...

    def annotations_dataframe(
        self,
        annotation_set_id: Union[ID, str],
        groups: List[str] = [],
        annotation_types: List[AnnotationType] = [AnnotationType.Box2d],
        progress: Optional[Progress] = None,
    ) -> DataFrame:
        """
        Get the AnnotationGroup for the specified annotation set with the
        requested annotation types.  The annotation type is used to filter
        the annotations returned.  Images which do not have any annotations
        are included in the result.

        The result is a DataFrame following the EdgeFirst Dataset Format
        definition.

        To get the annotations as a vector of AnnotationGroup objects, use the
        `annotations` method instead.

        Args:
            annotation_set_id (Union[ID, str]): ID of the annotation set.
            groups (List[str]): Dataset groups to include.
            annotation_types (List[AnnotationType]): Types of annotations to
                                                     include.
            progress (Optional[Sender[Progress]]): Optional progress channel.

        Returns:
            DataFrame: A Polars DataFrame containing the annotations.
        """
        ...

    def samples(
        self,
        dataset_id: Union[ID, str],
        annotation_set_id: Optional[ID] = None,
        annotation_types: List[AnnotationType] = [AnnotationType.Box2d],
        groups: List[str] = [],
        types: List[FileType] = [FileType.Image],
        progress: Optional[Progress] = None,
    ) -> List[Sample]:
        """
        Retrieve sample metadata and annotations for a dataset.

        Args:
            dataset_id (Union[ID, str]): ID of the dataset.
            annotation_set_id (Union[ID, str]): The ID of the annotation
                                                set to fetch.
            annotation_types (List[AnnotationType]): Types of annotations
                                                        to include.
            groups (List[str]): Dataset groups to include.
            types (List[FileType]): Type of files to include.
            progress (Optional[Progress]): Optional progress reporter.

        Returns:
            List[Sample]: A list of sample objects.
        """
        ...

    def experiments(self,
                    project_id: Union[ID, str],
                    name: Optional[str] = None) -> List[Experiment]:
        """
        Returns a list of experiments available to the user.  The experiments
        are returned as a vector of Experiment objects.  Experiments provide a
        method of organizing training and validation sessions together and are
        akin to an Experiment in MLFlow terminology.  Each experiment can have
        multiple trainer sessions associated with it, these would be akin to
        runs in MLFlow terminology.

        Args:
            project_id (Union[ID, str]): The ID of the project for
                              which to list experiments.
            name (Optional[str]): The name of the experiment to filter by.

        Returns:
            List[Experiment]: A list of Experiment objects
                              associated with the project.

        Raises:
            Error: If the server request fails.
        """
        ...

    def experiment(self, experiment_id: Union[ID, str]) -> Experiment:
        """
        Return the experiment with the specified experiment ID.  If the
        experiment does not exist, an error is returned.

        Args:
            experiment_id (Union[ID, str]): The ID of the experiment to fetch.

        Returns:
            Experiment: The Experiment object corresponding to the given ID.

        Raises:
            Error: If the experiment does not exist or request fails.
        """
        ...

    def training_sessions(self,
                          trainer_id: Union[ID, str],
                          name: Optional[str] = None) -> List[TrainingSession]:
        """
        Returns a list of trainer sessions available to the user.  The trainer
        sessions are returned as a vector of TrainingSession objects.  Trainer
        sessions are akin to runs in MLFlow terminology.  These represent an
        actual training session which will produce metrics and model artifacts.

        Args:
            trainer_id (Union[ID, str]): The ID of the trainer/experiment.
            name (Optional[str]): The name of the trainer session to filter by.

        Returns:
            List[TrainingSession]: A list of trainer sessions
                                  under the experiment.

        Raises:
            Error: If the request fails.
        """
        ...

    def training_session(self,
                         session_id: Union[ID, str]) \
            -> TrainingSession:
        """
        Return the training session with the specified training session ID.  If
        the training session does not exist, an error is returned.

        Args:
            session_id (Union[ID, str]): The ID of the training session.

        Returns:
            TrainingSession: The training session with the specified ID.

        Raises:
            Error: If the session does not exist or the request fails.
        """
        ...

    def validation_sessions(self,
                            project_id: Union[ID, str]) \
            -> List[ValidationSession]:
        """
        Returns a list of validation sessions associated with the specified
        project.

        Args:
            project_id (Union[ID, str]): The ID of the project to retrieve
            validation sessions for.

        Returns:
            List[ValidationSession]: A list of validation session objects.

        Raises:
            Error: If the request fails.
        """
        ...

    def validation_session(self,
                           session_id: Union[ID, str]) -> ValidationSession:
        """Return the validation session with the specified ID.

        Args:
            session_id (Union[ID, str]): The ID of the validation session.

        Returns:
            ValidationSession: The validation session with the specified ID.

        Raises:
            Error: If the validation session does not exist or the request
                   fails.
        """
        ...

    def artifacts(self, session_id: Union[ID, str]) -> List[Artifact]:
        """
        List the artifacts for the specified training session.  The artifacts
        are returned as a vector of strings.

        Args:
            session_id (Union[ID, str]): The ID of the training session.

        Returns:
            List[Artifact]: A list of artifact objects
                            generated by the session.

        Raises:
            Error: If the request fails.
        """
        ...

    def download_artifact(
        self,
        training_session_id: Union[ID, str],
        modelname: str,
        filename: Optional[Path] = None,
        progress: Optional[Progress] = None,
    ) -> None:
        """
        Download the model artifact for the specified trainer session to the
        specified file path.  A progress callback can be provided to monitor
        the progress of the download over a watch channel.

        Args:
            training_session_id (Union[ID, str]): ID of the trainer session the
                                      model belongs to.
            modelname (str): Name of the model file to download.
            filename (Optional[Path]): Local file path to save the downloaded
                                       artifact.  If not specified, the
                                       modelname is used as the filename.
            progress (Optional[Progress]): Optional progress callback.

        Raises:
            Error: If the download fails or cannot be written to disk.
        """
        ...

    def download_checkpoint(
        self,
        training_session_id: Union[ID, str],
        checkpoint: str,
        filename: Optional[Path] = None,
        progress: Optional[Progress] = None,
    ) -> None:
        """
        Download the checkpoint file for the specified trainer session to the
        specified file path.  A progress callback can be provided to monitor
        the progress of the download over a watch channel.

        Args:
            training_session_id (Union[ID, str]): ID of the trainer session the
                                      checkpoint belongs to.
            checkpoint (str): Name of the checkpoint file to download.
            filename (Optional[Path]): Local file path to save the downloaded
                                       checkpoint.  If not specified, the
                                       checkpoint name is used as the filename.
            progress (Optional[Progress]): Optional progress callback.

        Raises:
            Error: If the download fails or cannot be written to disk.
        """
        ...

    def tasks(self,
              name: Optional[str] = None,
              workflow: Optional[str] = None,
              status: Optional[str] = None,
              manager: Optional[str] = None) -> List[Task]:
        """
        Returns a list of tasks available to the user.  The tasks are returned
        as a vector of Task objects.  Tasks represent some workflow within
        EdgeFirst Studio such as trainer or validation sessions.  The managers
        represent where the task is run such as cloud, or user-managed, or
        kubernetes for on-premise installations.

        Args:
            name (Optional[str]): The name of the task to filter by.
            workflow (Optional[str]): The workflow name to filter by.
            status (Optional[str]): The status to filter by.
            manager (Optional[str]): The task manager to filter by.

        Returns:
            List[Task]: A list of Task objects.

        Raises:
            Error: If the server request fails.
        """
        ...

    def task_info(self, task_id: Union[ID, str]) -> TaskInfo:
        """
        Returns detailed information about a specific task.

        Args:
            task_id (Union[ID, str]): The ID of the task to retrieve.

        Returns:
            TaskInfo: The TaskInfo object containing detailed information.

        Raises:
            Error: If the task does not exist or the request fails.
        """
        ...

    def task_status(self, task_id: Union[ID, str], status: str) -> Task:
        """
        Updates the task status.

        Args:
            task_id (Union[ID, str]): The ID of the task to update.
            status (str): The new status to set for the task.

        Returns:
            Task: The updated Task object.

        Raises:
            Error: If the task does not exist or the request fails.
        """
        ...

    def set_stages(self,
                   task_id: Union[ID, str],
                   stages: List[Tuple[str, str]]) -> None:
        """
        Configures the task stages.  Stages are used to show various steps in
        the task execution process.

        Args:
            task_id (Union[ID, str]): The ID of the task to update.
            stages (Dict[str, str]): A dictionary representing the new stages
                                      for the task.

        Returns:
            None

        Raises:
            Error: If the task does not exist or the request fails.
        """
        ...

    def update_stage(self,
                     task_id: Union[ID, str],
                     stage: str,
                     status: str,
                     message: str,
                     percentage: int) -> None:
        """
        Updates a specific stage of a task.

        Args:
            task_id (Union[ID, str]): The ID of the task to update.
            stage (str): The name of the stage to update.
            status (str): The new status of the stage.
            message (str): A message describing the current state of the stage.
            percentage (int): The completion percentage of the stage (0-100).

        Returns:
            None

        Raises:
            Error: If the task or stage does not exist or the request fails.
        """
        ...
