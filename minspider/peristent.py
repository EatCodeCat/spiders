import sys
import logging


class Peristenter(object):
    """
       class of Saver, must include function working()
       """

    def __init__(self, save_pipe=sys.stdout):
        """
        constructor
        """
        self._save_pipe = save_pipe  # default: sys.stdout, also can be a file handler
        return

    def working(self, item: dict) -> bool:
        """
        working function, must "try, except" and don't change the parameters and return
        :return save_result: True or False
        """
        try:
            save_result = self.item_save(item)
        except Exception as excep:
            save_result = False
            logging.error("%s error: %s", self.__class__.__name__, excep,)

        logging.debug("%s end: save_result=%s, url=%s", self.__class__.__name__, save_result)
        return save_result

    def item_save(self, item: dict) -> bool:
        """
        save the item of a url, you can rewrite this function, parameters and return refer to self.working()
        """
        self._save_pipe.write("\t".join([str(i) for i in item.items()]) + "\n")
        self._save_pipe.flush()
        return True
