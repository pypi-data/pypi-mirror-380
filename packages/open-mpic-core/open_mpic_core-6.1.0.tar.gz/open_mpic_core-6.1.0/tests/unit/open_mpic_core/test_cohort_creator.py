import yaml
import hashlib
import pytest

from importlib import resources
from itertools import chain, cycle
from pydantic import TypeAdapter

from open_mpic_core import CohortCreator, RemotePerspective
from open_mpic_core.common_domain.enum.regional_internet_registry import RegionalInternetRegistry


# noinspection PyMethodMayBeStatic
class TestCohortCreator:
    @classmethod
    def setup_class(cls):
        cls.all_perspectives_per_rir = TestCohortCreator.set_up_perspectives_per_rir_dict_from_file()
        cls.all_perspectives = list(chain.from_iterable(cls.all_perspectives_per_rir.values()))
        cls.all_possible_perspectives_by_code = {perspective.code: perspective for perspective in cls.all_perspectives}

    # fmt: off
    @pytest.mark.parametrize("perspective_codes", [
        (['us-east-1', 'us-west-1', 'ca-west-1', 'eu-west-1', 'eu-central-1', 'ap-southeast-1',])
    ])
    # fmt: on
    def shuffle_available_perspectives_per_rir__should_return_dict_of_remote_perspective_lists(self, perspective_codes):
        perspectives = [
            self.all_possible_perspectives_by_code[perspective_code] for perspective_code in perspective_codes
        ]
        test_random_seed = hashlib.sha256("test1hash2seed3".encode("ASCII")).digest()
        shuffled_perspectives_per_rir = CohortCreator.shuffle_available_perspectives_per_rir(
            perspectives, test_random_seed
        )
        # get all rirs from named perspectives
        # convert list to set
        expected_perspectives_per_rir = {
            RegionalInternetRegistry.ARIN: ["us-east-1", "us-west-1", "ca-west-1"],
            RegionalInternetRegistry.APNIC: ["ap-southeast-1"],
            RegionalInternetRegistry.RIPE_NCC: ["eu-west-1", "eu-central-1"],
        }
        for rir in shuffled_perspectives_per_rir.keys():
            assert len(shuffled_perspectives_per_rir[rir]) == len(expected_perspectives_per_rir[rir])

    def shuffle_available_perspectives_per_rir__should_shuffle_perspectives_the_same_given_the_same_random_seed(self):
        shuffled_perspectives_per_rir_1 = CohortCreator.shuffle_available_perspectives_per_rir(
            self.all_perspectives, b"testSeedX"
        )
        shuffled_perspectives_per_rir_2 = CohortCreator.shuffle_available_perspectives_per_rir(
            self.all_perspectives, b"testSeedX"
        )
        shuffled_perspectives_per_rir_3 = CohortCreator.shuffle_available_perspectives_per_rir(
            self.all_perspectives, b"testSeedY"
        )
        # expect 1 and 2 to be identically sorted, while 3 should be different
        assert all(
            shuffled_perspectives_per_rir_1[rir] == shuffled_perspectives_per_rir_2[rir]
            for rir in shuffled_perspectives_per_rir_1.keys()
        )
        for rir in shuffled_perspectives_per_rir_1.keys():
            assert all(
                shuffled_perspectives_per_rir_1[rir][i] == shuffled_perspectives_per_rir_2[rir][i]
                for i in range(len(shuffled_perspectives_per_rir_1[rir]))
            )
        assert any(
            shuffled_perspectives_per_rir_1[rir] != shuffled_perspectives_per_rir_3[rir]
            for rir in shuffled_perspectives_per_rir_1.keys()
        )

    def shuffle_available_perspectives_per_rir__should_return_empty_dict_given_no_perspectives(self):
        shuffled_perspectives_per_rir = CohortCreator.shuffle_available_perspectives_per_rir([], b"testSeed")
        assert len(shuffled_perspectives_per_rir.keys()) == 0

    def shuffle_available_perspectives_per_rir__should_enrich_each_with_name_and_list_of_too_close_perspectives(self):
        perspective_codes = ["us-east-1", "us-west-1", "ca-west-1", "eu-west-1", "eu-central-1", "ap-southeast-1"]
        perspectives = [
            self.all_possible_perspectives_by_code[perspective_code] for perspective_code in perspective_codes
        ]
        shuffled_perspectives_per_rir = CohortCreator.shuffle_available_perspectives_per_rir(perspectives, b"testSeed")
        shuffled_perspectives_flattened = list(chain.from_iterable(shuffled_perspectives_per_rir.values()))
        assert all(perspective.name is not None for perspective in shuffled_perspectives_flattened)
        assert any(len(perspective.too_close_codes) > 0 for perspective in shuffled_perspectives_flattened)

    def create_perspective_cohorts__should_raise_exception_if_requested_cohort_size_is_less_than_2(self):
        with pytest.raises(Exception):
            CohortCreator.create_perspective_cohorts(self.all_perspectives_per_rir, 1)

    @pytest.mark.parametrize(
        "perspectives_per_rir, any_perspectives_too_close, cohort_size",
        [
            # perspectives_per_rir expects: (total_perspectives, total_rirs, max_per_rir, too_close_flag)
            ((3, 2, 2, False), False, 2),  # expect 1 cohort of 2
            ((6, 3, 2, False), False, 2),  # expect 3 cohorts of 2
            ((6, 3, 2, True), True, 2),  # expect 3 cohorts of 2
            ((6, 1, 6, False), False, 2),  # expect 3 cohorts of 2
            ((10, 2, 5, False), False, 5),  # expect 2 cohorts of 5
            ((10, 2, 5, True), True, 5),  # expect 1 cohort of 5
            ((10, 2, 5, True), True, 4),  # expect 2 cohorts of 4
            ((18, 5, 8, True), True, 6),  # expect 3 cohorts of 6
            ((18, 5, 8, False), False, 6),  # expect 3 cohorts of 6
            ((18, 3, 6, True), True, 6),  # expect 3 cohorts of 6
            ((18, 5, 7, True), True, 15),  # expect 1 cohort of 15
        ],
        indirect=["perspectives_per_rir"],
    )
    def create_perspective_cohorts__should_return_set_of_cohorts_with_requested_size(
        self, perspectives_per_rir, any_perspectives_too_close, cohort_size
    ):
        total_perspectives = len(list(chain.from_iterable(perspectives_per_rir.values())))
        # print(f"\ntotal perspectives: {total_perspectives}")
        # print(f"total rirs: {len(perspectives_per_rir.keys())}")
        # print(f"any perspectives too close: {any_perspectives_too_close}")
        # pprint(perspectives_per_rir)
        cohorts = CohortCreator.create_perspective_cohorts(perspectives_per_rir, cohort_size)
        # print(f"total cohorts created: {len(cohorts)}")
        # pprint(cohorts)
        assert len(cohorts) > 0
        if not any_perspectives_too_close:  # if no perspectives were too close, should have max possible cohorts
            assert len(cohorts) == total_perspectives // cohort_size
        for cohort in cohorts:
            assert len(cohort) == cohort_size
            # assert that no two perspectives in the cohort are too close to each other
            for i in range(len(cohort)):
                for j in range(i + 1, len(cohort)):
                    assert not cohort[i].is_perspective_too_close(cohort[j])
            # assert that all cohorts have at least 2 RIRs (unless desired cohort size is 2)
            if cohort_size > 2:
                assert len(set(map(lambda perspective: perspective.rir, cohort))) >= 2

    @pytest.mark.parametrize(
        "perspectives_per_rir, cohort_size",
        [
            # perspectives_per_rir expects: (total_perspectives, total_rirs, max_per_rir, too_close_flag)
            ((3, 1, 3, False), 3),  # expect 0 cohorts due to too few rirs
            ((3, 2, 2, True), 3),  # expect 0 cohorts due to too close perspectives
            ((18, 5, 8, True), 18),  # expect 0 cohorts due to too close perspectives
        ],
        indirect=["perspectives_per_rir"],
    )
    def create_perspective_cohorts__should_return_0_cohorts_given_no_cohort_would_meet_requirements(
        self, perspectives_per_rir, cohort_size
    ):
        # print(f"\ntotal perspectives: {len(list(chain.from_iterable(perspectives_per_rir.values())))}")
        # print(f"total rirs: {len(perspectives_per_rir.keys())}")
        # pprint(perspectives_per_rir)
        cohorts = CohortCreator.create_perspective_cohorts(perspectives_per_rir, cohort_size)
        assert len(cohorts) == 0

    def create_perspective_cohorts__should_handle_uneven_numbers_of_perspectives_per_rir(self):
        # 9 total perspectives, but can only make 2 cohorts of 3 perspectives each due to rir constraints
        perspectives_per_rir = {
            # 7 perspectives from apnic, 1 from ripe, 1 from arin
            RegionalInternetRegistry.APNIC: self.all_perspectives_per_rir[RegionalInternetRegistry.APNIC][:7],
            RegionalInternetRegistry.RIPE_NCC: self.all_perspectives_per_rir[RegionalInternetRegistry.RIPE_NCC][:1],
            RegionalInternetRegistry.ARIN: self.all_perspectives_per_rir[RegionalInternetRegistry.ARIN][:1],
        }  # 1 from arin
        cohorts = CohortCreator.create_perspective_cohorts(perspectives_per_rir, 3)
        assert len(cohorts) == 2

    @pytest.fixture
    def perspectives_per_rir(self, request):
        total_perspectives = request.param[0]
        total_rirs = request.param[1]
        max_per_rir = request.param[2]
        too_close_flag = request.param[3]
        return self.create_perspectives_per_rir_given_requirements(
            total_perspectives, total_rirs, max_per_rir, too_close_flag
        )

    def create_perspectives_per_rir_given_requirements(
        self, total_perspectives, total_rirs, max_per_rir, too_close_flag
    ):
        assert total_perspectives <= total_rirs * max_per_rir
        # get set (unique) of all rirs found in all_available_perspectives, each of which has a rir attribute
        perspectives_per_rir = dict[str, list[RemotePerspective]]()
        total_perspectives_added = 0
        # set ordered_rirs to be a list of rirs ordered in descending order based on number of perspectives for each rir in all_perspectives_per_rir
        all_rirs = list(self.all_perspectives_per_rir.keys())
        all_rirs.sort(key=lambda rir: len(self.all_perspectives_per_rir[rir]), reverse=True)
        while len(all_rirs) > total_rirs:
            all_rirs.pop()
        # in case total_perspectives is too high for the number actually available in the rirs left
        max_available_perspectives = sum(len(self.all_perspectives_per_rir[rir]) for rir in all_rirs)

        rirs_cycle = cycle(all_rirs)
        while total_perspectives_added < total_perspectives and total_perspectives_added < max_available_perspectives:
            current_rir = next(rirs_cycle)
            all_perspectives_for_rir: list[RemotePerspective] = list(self.all_perspectives_per_rir[current_rir])
            if current_rir not in perspectives_per_rir.keys():
                perspectives_per_rir[current_rir] = []
            while (
                len(perspectives_per_rir[current_rir]) < max_per_rir
                and len(all_perspectives_for_rir) > 0
                and total_perspectives_added < total_perspectives
            ):
                if too_close_flag and len(perspectives_per_rir[current_rir]) == 0:
                    # find two perspectives in all_perspectives_for_rir that are too close to each other
                    first_too_close_index = 0
                    first_too_close_perspective = None
                    second_too_close_index = 0
                    for i in range(len(all_perspectives_for_rir)):
                        if len(all_perspectives_for_rir[i].too_close_codes) > 0:
                            first_too_close_index = i
                            first_too_close_perspective = all_perspectives_for_rir[i]
                            break
                    for j in range(first_too_close_index + 1, len(all_perspectives_for_rir)):
                        if first_too_close_perspective.is_perspective_too_close(all_perspectives_for_rir[j]):
                            second_too_close_index = j
                            break
                    if second_too_close_index > 0:  # found two too close perspectives
                        # pop the later one first so that the earlier one is not affected by the index change
                        perspectives_per_rir[current_rir].append(all_perspectives_for_rir.pop(second_too_close_index))
                        perspectives_per_rir[current_rir].append(all_perspectives_for_rir.pop(first_too_close_index))
                        total_perspectives_added += 2
                        continue

                perspective_to_add = all_perspectives_for_rir.pop(0)
                if not any(
                    perspective_to_add.is_perspective_too_close(perspective)
                    for perspective in perspectives_per_rir[current_rir]
                ):
                    perspectives_per_rir[current_rir].append(perspective_to_add)
                    total_perspectives_added += 1
                else:
                    continue

        return perspectives_per_rir

    @staticmethod
    def set_up_perspectives_per_rir_dict_from_file():
        resource_files = resources.files("tests.resources")
        perspectives_yaml_file = resource_files.joinpath("test_region_config.yaml")
        with perspectives_yaml_file.open() as file:
            perspectives_yaml = yaml.safe_load(file)
            perspective_type_adapter = TypeAdapter(list[RemotePerspective])
            perspectives = perspective_type_adapter.validate_python(perspectives_yaml["available_cloud_regions"])
            # get set of unique rirs from perspectives, each of which has a rir attribute
            all_rirs = set(map(lambda perspective: perspective.rir, perspectives))
            return {rir: [perspective for perspective in perspectives if perspective.rir == rir] for rir in all_rirs}

    @staticmethod
    def convert_codes_to_remote_perspectives(
        perspective_codes: list[str], all_possible_perspectives_by_code: dict[str, RemotePerspective]
    ) -> list[RemotePerspective]:
        return [all_possible_perspectives_by_code[perspective_code] for perspective_code in perspective_codes]
