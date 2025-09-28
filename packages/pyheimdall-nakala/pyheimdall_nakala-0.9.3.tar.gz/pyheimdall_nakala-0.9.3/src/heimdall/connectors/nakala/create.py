# -*- coding: utf-8 -*-
import heimdall
import requests
from json import dumps
from .objects import Collection, Data, File
from .objects import PROD_URL, TEST_URL  # TODO remove

"""
Provides the Nakala CREATE connector.

:copyright: The pyHeimdall contributors.
:licence: Afero GPL, see LICENSE for more details.
:SPDX-License-Identifier: AGPL-3.0-or-later
"""  # nopep8: E501


@heimdall.decorators.create_database('api:nakala')
def upload(tree, **options):
    r"""Posts a HERA elements tree to the Nakala API

    :param tree: HERA elements tree
    :param url: Endpoint to POST to

    .. ERROR::
       This feature is not implemented yet.
       Reasons are partly a lack of resources, but mostly concerns about
       making public sharing of research data too straightforward and the
       worry that too much convenience would lead to a further decline in
       metadata quality.

       Interested readers can submit a request to further this topic.
       See the ``CONTRIBUTING`` file at the root of the pyHeimdall repository.
    """
    private = options.get('private', False)
    test = options.get('test', True)
    url = options.get('url', TEST_URL if test else PROD_URL)
    data_entities = options.get('datas', ['item', ])
    file_pid = options.get('files', ['file', ])
    strategy = options.get('metadata_strategy', None)
    api_key = '01234567-89ab-cdef-0123-456789abcdef'
    nkl_metas_creator = options.get('metadata_creator', create_nakala_metadata)

    def _has_nakala_uri(uris):  # TODO rename
        for uri in uris:
            if 'nakala.fr' in uri:
                return True
        return len(uris) == 1

    properties = heimdall.getProperties(tree, lambda e: _has_nakala_uri(e.uri))

    for item in heimdall.getItems(tree):
        if item.get('eid') not in data_entities:
            continue
        hashes = _upload_files(tree, item, api_key, test)
        metadata = _create_metadatas(item, properties, nkl_metas_creator)
        doi = _upload_item(tree, url, api_key, private, metadata, hashes)
        if doi is not None:
            heimdall.createMetadata(item, doi, pid='identifier', aid='doi')


def _upload_item(tree, baseurl, api_key, private, metadata, hashes):
    url = f'{baseurl}/datas'
    status = 'pending' if private else 'published'
    creators = []  # TODO use item.contributors {givenname, surname, }
    post_data = {
            'status': status,
            'collectionsIds': [],
            'files': [{'sha1': h, } for h in hashes],
            'rights': [],
            'metas': metadata,
            'creators': creators,
            }
    headers = {
            'X-API-KEY': api_key,
            'Content-Type': 'application/json',
            }
    response = requests.post(url, headers=headers, data=dumps(post_data))
    if response.status_code != requests.codes.created:
        # raise _exception(response)
        print(_exception(response))
        doi = None
    else:
        doi = response.json()['payload']['id']
    return doi


def _create_metadatas(item, properties, create_metadata):
    metadatas = list()
    publisher = heimdall.getValue(item, pid='publisher')
    for p in properties:  # iterate on properties to upload metadatas for
        values = heimdall.getValues(item, pid=p.get('id'))
        uri = _get_property_uri(p)
        for value in values:
            language = 'fr'  # TODO
            metas = create_metadata(uri, value, language)
            if type(metas) is list:
                metadatas.extend(metas)
            else:
                metadatas.append(metas)
    return metadatas


def _uri2typeUri(uri):
    if uri == 'http://nakala.fr/terms#type':
        return 'http://purl.org/dc/terms/URI'
    return None  # 'http://www.w3.org/2001/XMLSchema#string'


def create_nakala_metadata(uri, value, language):
    if uri == 'http://nakala.fr/terms#creator':
        return {
            'value': {'surname': value, 'givenname': ".", },
            'propertyUri': uri,
            }
    return {
            'value': value,
            'typeUri': _uri2typeUri(uri),
            'propertyUri': uri,
            }


def _get_property_uri(property):
    for uri in property.uri:
        if 'nakala.fr' in uri:
            return uri
    return property.uri[0]


def _upload_files(tree, item, api_key, test):
    f_pid = 'file'
    pointers = heimdall.getValues(item, pid=f_pid)

    def get_target(item):
        nonlocal pointer
        if heimdall.getValue(item, pid='path') == pointer:
            return True
        return False

    hashes = list()
    for pointer in pointers:
        f_item = heimdall.getItem(tree, get_target)
        f_path = heimdall.getValue(f_item, pid='path')
        f = File(f_path, test=test)
        sha = f.upload(api_key)
        heimdall.createMetadata(f_item, sha, pid='identifier', aid='sha1')
        hashes.append(sha)
    return hashes
