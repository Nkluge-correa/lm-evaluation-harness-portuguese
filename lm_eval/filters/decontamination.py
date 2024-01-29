from lm_eval.api.filter import Filter
import re

class DecontaminationFilter(Filter):

    """
    A filter which evaluates
    """

    name = "track_decontamination"

    def __init__(self, path) -> None:
        """

        TODO: make sure only ever run one time on the train set (should this be cached as a class var? keyed by value for "path").
        should further cache result on a given (task_name, doc_id)
        """
        self._decontam_results = None

    def apply(self, resps, docs) -> None:
        """
        Return {"no_contamination", "only_contamination"} keys for the 2 different subsets
        """
        pass

class NormalizeSpacesFilter(Filter):

    def __init__(self) -> None:
        pass

    def remove_extra_spaces(self, text):
        text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
        text = re.sub(' +', ' ', text)
        return text.strip()

    def apply(self, resps, docs) -> None:
        def filter_set(inst):
            return [self.remove_extra_spaces(resp) for resp in inst]
        return [filter_set(resp) for resp in resps]
