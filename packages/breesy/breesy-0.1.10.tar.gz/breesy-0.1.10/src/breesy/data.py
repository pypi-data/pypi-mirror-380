from urllib.request import urlopen, Request
import certifi, ssl
from shutil import copyfileobj
from pathlib import Path
from scipy.io import loadmat
# from mne.io import read_raw_edf

from .Recording import Recording
from .RecordingMetadata import RecordingMetadata
from .errors import BreesyError


def load_example_data(dataset_name: str, dir_name: str = "tmp", ssl_context=None) -> Recording:
    """Load example EEG datasets for testing and learning.

    Downloads and loads publicly available EEG data files. Currently available datasets include:
    'alpha', 'madhd', 'pangolin'.

    :param dataset_name: Name of the dataset to load
    :param dir_name: Directory to save downloaded files
    :param ssl_context: SSL context for secure downloads

    :return: Recording object containing the loaded example data
    """

    available_datasets = ['alpha', 'madhd', 'pangolin']

    # TODO: some downloads take time, do some loading bar?
    if dataset_name == "alpha":
        filename = "subject_01.mat"
        url = "https://zenodo.org/records/2348892/files/subject_01.mat?download=1"
        ch_names = ["Fp1", "Fp2", "FC5", "FC6", "Fz", "T7", "Cz", "T8",
                    "P7", "P3", "Pz", "P4", "P8", "O1", "Oz", "O2"]
        sample_rate = 512

    elif dataset_name == "madhd":
        filename = "MADHD.mat"
        url = "https://data.mendeley.com/public-files/datasets/6k4g25fhzg/files/9c5928cf-f8ef-485b-ac5b-f17b2df935f3/file_downloaded"
        ch_names = ["Cz", "F4"]
        sample_rate = 256

    # elif dataset_name == "schalk":
    #     filename = "S001R01.edf"
    #     url = "https://www.physionet.org/files/eegmmidb/1.0.0/S001/S001R01.edf?download"
    #     ch_names = ['Fc5', 'Fc3', 'Fc1', 'Fcz', 'Fc2', 'Fc4', 'Fc6',
    #                 'C5', 'C3', 'C1', 'Cz', 'C2', 'C4', 'C6',
    #                 'Cp5', 'Cp3', 'Cp1', 'Cpz', 'Cp2', 'Cp4', 'Cp6',
    #                 'Fp1', 'Fpz', 'Fp2', 'Af7', 'Af3', 'Afz', 'Af4', 'Af8',
    #                 'F7', 'F5', 'F3', 'F1', 'Fz', 'F2', 'F4', 'F6', 'F8',
    #                 'Ft7', 'Ft8', 'T7', 'T8', 'T9', 'T10', 'Tp7', 'Tp8',
    #                 'P7', 'P5', 'P3', 'P1', 'Pz', 'P2', 'P4', 'P6', 'P8',
    #                 'Po7', 'Po3', 'Poz', 'Po4', 'Po8', 'O1', 'Oz', 'O2', 'Iz'
    #                 ]
    #     sample_rate = 160

    elif dataset_name == "pangolin":
        filename = "S1_run8.mat"
        url = "https://osf.io/download/jrcn8/?view_only=d23acfd50655427fbaae381a17cbfbcc"
        ch_names = [f"ch{i+1}" for i in range(258)]  # this dataset has no standard channel names
        sample_rate = 600

    # elif dataset_name == "telemetry":
    #     filename = "ST7011J0-PSG.edf"
    #     url = "https://www.physionet.org/files/sleep-edfx/1.0.0/sleep-telemetry/ST7011J0-PSG.edf?download"
    #     ch_names = range(5)  # TODO: get actual channel names
    #     sample_rate = 100

    else:
        available_datasets_string = ", ".join([f'"{n}"' for n in available_datasets])
        raise BreesyError(f'Unknown name of dataset provided: "{dataset_name}".', 
                          f'Use one of available dataset names ({available_datasets_string}).')

    dirpath = Path(dir_name)
    dirpath.mkdir(parents=True, exist_ok=True)
    filepath = dirpath / filename

    if not filepath.exists():  # TODO: use temp download location instead of working dir
        print(f'Will download the data file from {url}')
        if ssl_context is None:
            ssl_context = ssl.create_default_context(cafile=certifi.where())
        req = Request(url, headers={'User-Agent' : "Magic Browser"}) 
        with urlopen(req, context=ssl_context) as in_stream, open(filepath, 'wb') as out_file:
            copyfileobj(in_stream, out_file)
        print(f'Done! Save file in: {filepath}')

    if dataset_name == "alpha":
        data = loadmat(filepath)["SIGNAL"].T[1:-2]  # removes non-EEG channels
    elif dataset_name == "madhd":
        data = loadmat(filepath, squeeze_me=True)['MADHD'][0][0, :, :].T  # leaves one recording only
    elif dataset_name == "pangolin":
        data = loadmat(filepath, squeeze_me=True)['y']
    elif dataset_name in ["schalk", "telemetry"]:
        # data = read_raw_edf(filepath, verbose=0).get_data()  # TODO: remove MNE requirement
        raise ValueError(f'The "{dataset_name}" is temporarily unsupported as it is an EDF file and requires MNE to be loaded.')

    metadata = RecordingMetadata(
        name=Path(filename).stem,
        file_path=filepath,
        description=f"Sample dataset: {dataset_name}"
    )

    recording = Recording(
        data=data,
        channel_names=ch_names,
        sample_rate=sample_rate,
        events=None,
        metadata=metadata
    )

    return recording