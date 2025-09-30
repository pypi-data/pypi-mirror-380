import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd
from cehrbert.runners.hf_runner_argument_dataclass import DataTrainingArguments
from datasets import Dataset

from cehrgpt.runners.data_utils import create_dataset_splits
from cehrgpt.runners.hf_gpt_runner_argument_dataclass import CehrGPTArguments


# Mock dataset loading function
def load_parquet_as_dataset(folder_path):
    # Create a mock dataset
    data = {
        "index_date": np.random.choice(
            np.arange("2021-01-01", "2022-01-01", dtype="datetime64[D]"), 100
        ),
        "person_id": np.random.randint(1, 20, 100),
    }
    # Convert the Pandas dataframe to a Hugging Face dataset
    return Dataset.from_pandas(pd.DataFrame(data, columns=["person_id", "index_date"]))


class TestCreateDatasetSplits(unittest.TestCase):

    @patch(
        "cehrgpt.runners.data_utils.load_parquet_as_dataset",
        side_effect=load_parquet_as_dataset,
    )
    def test_split_by_patient(self, mock_load_dataset):
        # Test patient-based split
        data_args = DataTrainingArguments(
            data_folder="data/",
            dataset_prepared_path="prepared_data/",
            split_by_patient=True,
            validation_split_percentage=0.2,
        )
        cehrgpt_args = CehrGPTArguments(patient_splits_path=None)
        train_set, validation_set, test_set = create_dataset_splits(
            data_args, cehrgpt_args=cehrgpt_args, seed=42
        )

        # Verify that patients are unique across splits
        train_patient_ids = set(train_set["person_id"])
        val_patient_ids = set(validation_set["person_id"])
        test_patient_ids = set(test_set["person_id"])

        self.assertTrue(
            train_patient_ids.isdisjoint(val_patient_ids),
            "Patients overlap between train and validation sets",
        )
        self.assertTrue(
            train_patient_ids.isdisjoint(test_patient_ids),
            "Patients overlap between train and test sets",
        )
        self.assertTrue(
            val_patient_ids.isdisjoint(test_patient_ids),
            "Patients overlap between validation and test sets",
        )


if __name__ == "__main__":
    unittest.main()
