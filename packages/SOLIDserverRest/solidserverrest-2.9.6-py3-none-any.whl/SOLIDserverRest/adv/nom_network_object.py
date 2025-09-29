#
# pylint: enable=R0801

"""
SOLIDserver NOM network object (device)

"""
from __future__ import annotations

import logging

from SOLIDserverRest.Exception import (SDSError, SDSInitError)

from .class_params import ClassParams
from .nom_folder import NomFolder


class NomNetObject(ClassParams):
    """ class to manipulate the SOLIDserver NOM network object (aka device) """

    # -------------------------------------
    def __init__(self,
                 sds=None,
                 name=None,
                 folder=None,
                 class_params=None):
        """init a NOM network object:
        - sds: object SOLIDserver, could be set afterwards
        """

        self.clean_params()

        if not name:
            raise SDSError(
                message=f"name is required for network object")

        super().__init__(sds, name)

        if not folder:
            raise SDSError(
                message=f"folder is required for network object {name}")

        if not isinstance(folder, NomFolder):
            raise SDSError(
                message=f"folder is not a correct object for {name}")

        self.folder = folder

        if class_params is not None:
            self.set_class_params(class_params)

    # -------------------------------------
    def clean_params(self):
        """ clean the object params """
        super().clean_params()

        self.parent = None
        self.folder = None
        self.type = None
        self.state = None
        self.description = None

    # -------------------------------------
    def set_parent(self, parent: NomNetObject):
        """ set a parent object for this object """
        if parent and not isinstance(parent, NomNetObject):
            raise SDSError(
                message=f"parent object {parent} not of type NomNetObject")

        self.parent = parent

    # -------------------------------------
    def set_type(self, _type=None):
        """ set a type for this object """
        if _type and not isinstance(_type, str):
            raise SDSError(
                message=f"type should be a string")

        self.type = _type

    # -------------------------------------
    def set_state(self, _state=None):
        """ set a state for this object """
        if _state and not isinstance(_state, str):
            raise SDSError(
                message=f"state should be a string")

        self.state = _state

    # -------------------------------------
    def set_description(self, _descr=None):
        """ set a description for this object """
        if _descr and not isinstance(_descr, str):
            raise SDSError(
                message=f"description should be a string")

        self.description = _descr

    # -------------------------------------
    def create(self):
        """ create the network object """

        if self.sds is None:
            raise SDSError(message="not connected")

        # if object already created
        if self.myid > 0:
            return

        if not self.folder:
            raise SDSInitError(
                message="missing folder to create the NOM object")

        params = {
            'nomfolder_id': self.folder.myid,
            **self.additional_params
        }

        if self.name is not None:
            params['nomnetobj_name'] = self.name
        else:
            raise SDSInitError(message="missing name to NOM object")

        if self.parent:
            params['parent_nomnetobj_id'] = self.parent.myid

        if self.type:
            params['nomnetobj_type'] = self.type
        if self.state:
            params['nomnetobj_state'] = self.state
        if self.description:
            params['nomnetobj_description'] = self.description

        self.prepare_class_params('nomnetobj', params)

        # logging.info(params)

        rjson = self.sds.query("nom_netobj_create",
                               params=params)

        if 'errmsg' in rjson:
            raise SDSError(message="network object creation, "
                           + rjson['errmsg'])

        self.params['nomnetobj_id'] = int(rjson[0]['ret_oid'])
        self.myid = int(self.params['nomnetobj_id'])

        self.refresh()

    # -------------------------------------
    def get_id_by_fullname(self, fullname):
        """get the ID of the network object in current folder,
           return None if non existant"""

        params = {
            "limit": 1,
            **self.additional_params
        }
        _where = f"nomfolder_id={self.folder.myid}"
        _where += f" AND nomnetobj_name='{fullname}'"
        params.update({"WHERE": _where})

        try:
            rjson = self.sds.query('nom_netobj_list',
                                   params=params)
        except SDSError as err_descr:
            msg = f"cannot found NOM object by name {fullname}"
            msg += " / " + str(err_descr)
            raise SDSError(msg) from err_descr

        if rjson[0]['errno'] != '0':  # pragma: no cover
            raise SDSError("errno raised on get network object")

        return rjson[0]['nomnetobj_id']

    # -------------------------------------
    def refresh(self):
        """refresh content of the NOM object from the SDS"""

        if self.sds is None:
            raise SDSError(message="not connected")

        try:
            nomnetobj_id = self.get_id_by_fullname(fullname=f"{self.name}")
        except SDSError as err_descr:
            msg = "cannot get NOM object id"
            msg += " / " + str(err_descr)
            raise SDSError(msg) from err_descr

        params = {
            "nomnetobj_id": nomnetobj_id,
            **self.additional_params
        }

        rjson = self.sds.query("nom_netobj_info",
                               params=params)

        rjson = rjson[0]

        self.myid = int(rjson['nomnetobj_id'])

        for label in ['nomnetobj_id',
                      'parent_nomnetobj_id',
                      'nomnetobj_class_name',
                      'nomnetobj_path',
                      'parent_nomnetobj_name',
                      'parent_nomfolder_path',
                      'nomnetobj_nb_iface',
                      'nomnetobj_nb_connected_ports',
                      'nomnetobj_main_iface',
                      'nomnetobj_main_iface_hostaddr',
                      'nomnetobj_main_iface6',
                      'nomnetobj_main_iface6_hostaddr']:
            if label not in rjson:   # pragma: no cover
                raise SDSError(f"parameter {label} not found in NOM object")
            self.params[label] = rjson[label]

        if 'nomnetobj_class_parameters' in rjson:   # pragma: no cover
            self.update_class_params(rjson['nomnetobj_class_parameters'])

        if 'nomnetobj_description' in self.params:
            self.description = self.params['nomnetobj_description']

        if 'nomnetobj_type' in rjson:
            self.set_type(rjson['nomnetobj_type'])
        if 'nomnetobj_state' in rjson:
            self.set_state(rjson['nomnetobj_state'])

    # -------------------------------------
    def set_param(self, param=None, value=None, exclude=None, name=None):
        """ set a specific param on the NOM object object """
        super().set_param(param,
                          value,
                          exclude=['nomnetobj_id',
                                   'nomfolder_id',
                                   'parent_nomnetobj_id'],
                          name='name')

    # -------------------------------------
    def delete(self):
        """deletes the NOM netobj in the SDS"""
        if self.sds is None:
            raise SDSError(message="not connected")

        if self.myid == -1:
            raise SDSError("on NOM netobj delete")

        params = {
            'nomnetobj_id': self.myid,
            **self.additional_params
        }

        _r = self.sds.query("nom_netobj_delete",
                            params=params)

        self.clean_params()

    # -------------------------------------
    def update(self):
        """ update the NOM object in SDS """

        if self.sds is None:
            raise SDSError(message="not connected")

        params = {
            'nomnetobj_id': self.myid,
            **self.additional_params
        }

        if self.type:
            params['nomnetobj_type'] = self.type
        else:
            params['nomnetobj_type'] = ''

        if self.state:
            params['nomnetobj_state'] = self.state
        else:
            params['nomnetobj_state'] = ''

        if self.description:
            params['nomnetobj_description'] = self.description
        else:
            params['nomnetobj_description'] = ''

        self.prepare_class_params('nomnetobj', params)

        # logging.info(params)

        rjson = self.sds.query("nom_netobj_update",
                               params=params)

        if 'errmsg' in rjson:  # pragma: no cover
            raise SDSError(message="NOM object update error, "
                           + rjson['errmsg'])

        self.refresh()

    # -------------------------------------
    def __str__(self):  # pragma: no cover
        """return the string notation of the NOM object"""

        return_val = "*NOM netobj* "

        if self.name:
            return_val += f"{self.name}"
        else:
            return_val += f"NOT_SET"

        if self.type:
            return_val += f" type: {self.type}"

        if self.state:
            return_val += f" state: {self.state}"

        if self.description:
            return_val += f" description: '{self.description}'"

        if self.parent:
            return_val += f" parent: {self.parent.name}"

        if 'nomnetobj_nb_iface' in self.params:
            if int(self.params['nomnetobj_nb_iface']) > 0:
                return_val += f" interface={self.params['nomnetobj_nb_iface']}"

        if 'nomnetobj_nb_connected_ports' in self.params:
            if int(self.params['nomnetobj_nb_connected_ports']) > 0:
                return_val += f" ports={self.params['nomnetobj_nb_connected_ports']}"

        return_val += self.str_params(exclude=['nomnetobj_id',
                                               'name',
                                               'parent_nomnetobj_name',
                                               'parent_nomnetobj_id',
                                               'nomnetobj_nb_iface',
                                               'nomnetobj_nb_connected_ports'])

        return_val += str(super().__str__())

        return return_val
