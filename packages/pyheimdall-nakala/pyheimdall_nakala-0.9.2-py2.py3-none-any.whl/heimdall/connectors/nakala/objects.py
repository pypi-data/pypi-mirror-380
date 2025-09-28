# -*- coding: utf-8 -*-
import requests
import hashlib
import mimetypes
from json import dumps, loads

"""
Provides utility classes for CRUD operations with Nakala.

:copyright: The pyHeimdall contributors.
:licence: Afero GPL, see LICENSE for more details.
:SPDX-License-Identifier: AGPL-3.0-or-later
"""  # nopep8: E501

PROD_URL = 'https://api.nakala.fr'
TEST_URL = 'https://apitest.nakala.fr'


def _exception(response):
    errors = loads(response.text)
    message = errors['message']
    if type(errors.get('payload', None)) is dict:
        for m in errors['payload']['validationErrors']:
            message += f"\n - {m}"
    trace = '[%s] %s:\n%s' % (response.status_code, response.url, message)
    return requests.exceptions.HTTPError(trace, response=response)


class Uploadable(object):
    f"""Abstract class for all Nakala "objects"

    :see also: :py:class:`heimdall.connectors.nakala.Collection`
    :see also: :py:class:`heimdall.connectors.nakala.Data`
    :see also: :py:class:`heimdall.connectors.nakala.File`
    """

    def __new__(cls, *args, **kwargs):
        """Abstract class method, do not call directly kthxbye
        """
        if cls is Uploadable:
            raise TypeError("Class {cls.__name__} is meant to be abstract")
        return super().__new__(cls)

    def __init__(self, test=True):
        r"""Uploadable constructor

        :param test: (:py:class:`bool`, default: ``True``) -- If ``True``, Nakala test server will be used.
        """  # nopep8: E501
        if isinstance(test, bool) and not test:  # `False` and nothing else
            self.baseurl = PROD_URL
        else:  # anything else
            self.baseurl = TEST_URL
        self._delete_success_code = requests.codes.no_content

    def delete(self, api_key):
        r"""Deletes this object from Nakala

        :param api_key: (:py:class:`str`) -- Nakala API key
        :return: HTTP Response
        :rtype: :py:class:`requests.Response`
        """
        if not hasattr(self, 'id'):
            return  # nothing to do

        url = f'{self.url}/{self.id}'
        headers = {
            'X-API-KEY': api_key,
            'accept': 'application/json',
            }
        response = requests.delete(url, headers=headers)
        if response.status_code == self._delete_success_code:
            delattr(self, 'id')
            return response
        raise _exception(response)


class Collection(Uploadable):
    f"""Nakala "Collection"
    """

    def __init__(self, title, rights=None, private=True, test=True):
        r"""Uploadable Collection constructor

        :param title: (:py:class:`str`) -- Collection human-readable name
        :param rights: (:py:class:`list`) -- Who has which rights on the Collection ; if left empty, only the uploader will have iwner rights ; see Nakala API documentation for details
        :param private: (:py:class:`bool`, default: ``True``) -- If ``False``, the Collection will be publicly viewable.
        :param test: (:py:class:`bool`, default: ``True``) -- If ``True``, Nakala test server will be used.
        """  # nopep8: E501
        super(Collection, self).__init__(test)
        self.url = f'{self.baseurl}/collections'
        self.title = title
        self.rights = rights or []
        self.status = 'private' if private else 'public'

    def upload(self, api_key):
        r"""Creates this Collection on Nakala

        :param api_key: (:py:class:`str`) -- Nakala API key
        :return: Collection unique identifer (*aka* Nakala handle)
        :rtype: :py:class:`str`

        At the time of writing, although unique on Nakala, collection identifiers are *not* DOIs.
        """  # nopep8: E501
        if hasattr(self, 'id'):
            return self.id

        headers = {
            'X-API-KEY': api_key,
            'Content-Type': 'application/json',
            }
        data = {
            'status': self.status,
            'rights': self.rights,
            'metas': [{
                'value': self.title,
                # 'lang': None,
                # 'typeUri': 'http://www.w3.org/2001/XMLSchema#string',
                'propertyUri': 'http://nakala.fr/terms#title',
                }]
            }
        response = requests.post(self.url, headers=headers, data=dumps(data))
        if response.status_code == requests.codes.created:
            self.id = response.json()['payload']['id']
            return self.id
        raise _exception(response)


class Data(Uploadable):
    f"""Nakala "Data"
    """

    def __init__(self, metadata, files,
                 collections=None, rights=None, creators=None,
                 private=True, test=True):
        super(Data, self).__init__(test)
        self.url = f'{self.baseurl}/datas'
        self.metadata = metadata or []  # NOTE upload() fails if missing metas
        self.files = files or []  # NOTE: upload() fails if no file
        self.collections = collections or []
        self.rights = rights or []
        self.creators = creators or []
        self.status = 'pending' if private else 'published'

    def upload(self, api_key):
        if hasattr(self, 'id'):
            return self.id

        headers = {
            'X-API-KEY': api_key,
            'Content-Type': 'application/json',
            }
        data = {
            'status': self.status,
            'collectionsIds': self.collections,
            'files': [{'sha1': h, } for h in self.files],
            'rights': self.rights,
            'metas': self.metadata,
            'creators': self.creators,
            }
        response = requests.post(self.url, headers=headers, data=dumps(data))
        if response.status_code == requests.codes.created:
            self.id = response.json()['payload']['id']
            return self.id  # this is a DOI
        raise _exception(response)


class File(Uploadable):
    r"""Nakala "file upload"
    """

    def __init__(self, path, test=True):
        r"""Uploadable File constructor

        :param path: (:py:class:`str`) -- Absolute path to the file to be uploaded
        :param test: (:py:class:`bool`, default: ``True``) -- If ``True``, Nakala test server will be used.
        """  # nopep8: E501
        super(File, self).__init__(test)
        self.url = f'{self.baseurl}/datas/uploads'
        self.path = path
        self.CHUNK_SIZE = 65536
        self._delete_success_code = requests.codes.ok

    def upload(self, api_key, secure=True):
        r"""Uploads this file to Nakala

        :param api_key: (:py:class:`str`) -- Nakala API key
        :param secure: (:py:class:`bool`, default: ``True``) -- Secure mode
        :return: File SHA-1 understood by Nakala
        :rtype: :py:class:`str`

        If successful, this method returns the file's SHA, as it was returned by Nakala.

        However, this SHA is *not* guaranteed to be the local file's SHA
        (given by ``self.sha``), as network data loss or corruption can happen.
        If ``secure``parameter is ``True``, and both SHA differ, this method raises
        a :py:class:`requests.ConnectionError`, and this method should be called
        one more time.
        Set ``secure`` parameter to ``False`` to disable this behaviour.

        :see also: :py:class:`heimdall.connectors.nakala.File.sha`
        """  # nopep8: E501
        if hasattr(self, 'id'):
            return self.id

        headers = {
            'X-API-KEY': api_key,
            'accept': 'application/json',
            }
        with open(self.path, 'rb') as f:
            files = {'file': (self.path, f, self.mime)}
            response = requests.post(self.url, headers=headers, files=files)
        if response.status_code == requests.codes.created:
            self.id = response.json()['sha1']
            if secure and (self.id != self.sha):
                message = f"BAD SHA-1 expected: {self.sha} got: {self.id}"
                delattr(self, 'id')
                raise requests.ConnectionError(message, response=response)
            return self.id
        raise _exception(response)

    @property
    def sha(self):
        r"""Gets this file's SHA-1, computed locally

        So this doesn't break or fill up memory if file is huge, file is read
        in chunks ; chunk size is ``self.CHUNK_SIZE`` (default: 64Kb).
        """
        sha1 = hashlib.sha1()
        with open(self.path, 'rb') as f:
            while True:
                data = f.read(self.CHUNK_SIZE)
                if not data:
                    break
                sha1.update(data)
        return sha1.hexdigest()

    @property
    def mime(self):
        r"""Gets this file's media type (formerly MIME type)
        """
        return mimetypes.MimeTypes().guess_type(self.path)[0]
