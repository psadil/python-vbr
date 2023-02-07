from vbr.tableclasses import RcapTable, class_from_table

__all__ = ["RcapTableApi"]


class RcapTableApi(object):
    def create_redcap_table_row(
        self, redcap_form_name: str, redcap_data: dict, **kwargs
    ) -> RcapTable:
        """Create a RcapTable-derived VBR record."""
        # TODO = fix this in RcapTable. I don't like this construction
        PARAMS = list(RcapTable.link_column_names())
        PARAMS.append("record_id")
        # Look up the table class
        tc = class_from_table("rcap_" + redcap_form_name)
        # Extend redcap_data dictionary with any provided kwargs on the allow list
        for p in PARAMS:
            if kwargs.get(p, None) is not None:
                redcap_data[p] = kwargs.get(p)
                # print('kwarg found: ', p, redcap_data[p])
        # Instantiate the VBR object
        instance = tc(**redcap_data)
        return self.vbr_client.create_row(instance)[0]

    def get_redcap_record_by_biosample_and_instance(
        self, redcap_form_name: str, biosample_id: str, subject_id: str, protocol_id: str, repeat_instance: str
        ) -> RcapTable:
        """Retrieve a Biosample by subject and protocol IDs."""
        query = {
            "subject": {"operator": "=", "value": subject_id},
            "biosample": {"operator": "=", "value": biosample_id},
            "protocol": {"operator": "=", "value": protocol_id},
            "redcap_repeat_instance": {"operator": "=", "value": repeat_instance}
        }
        return self._get_row_from_table_with_query(redcap_form_name, query=query)

