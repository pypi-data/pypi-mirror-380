
from typing import List, Optional, Dict
from KeyisBTools.cryptography.sign import s2
from KeyisBTools.cryptography import m1

from ._app import GNRequest, GNResponse
from gnobjects.net.objects import Url

from KeyisBTools.cryptography.bytes import hash3

class KDCObject:
    def __init__(self, domain: str, kdc_domain: str, kdc_key: bytes, requested_domains: List[str]):
        self._domain = domain
        self._kdc_domain = kdc_domain
        self._kdc_key = kdc_key
        self._requested_domains = requested_domains

        from ._client import AsyncClient
        self._client = AsyncClient(domain)

        self._servers_keys: Optional[Dict[str, bytes]] = None
        self._servers_keys_hash_domain: Dict[bytes, str] = {}
        self._servers_keys_domain_hash: Dict[str, bytes] = {}




    async def init(self, servers_keys: Optional[Dict[str, bytes]] = None): # type: ignore
        if servers_keys is None:
                
            payload = self._requested_domains
            r = await self._client.request(GNRequest('GET', Url(f'gn://{self._kdc_domain}/api/sys/server/keys'), payload=payload))

            if not r.command.ok:
                raise r
            
            servers_keys: Dict[str, bytes] = r.payload
            
        self._servers_keys = servers_keys

        for domain in self._servers_keys.keys():
            h = hash3(domain.encode())
            self._servers_keys_hash_domain[h] = domain
            self._servers_keys_domain_hash[domain] = h


        self._servers_keys[self._kdc_domain] = self._kdc_key
        h = hash3(self._kdc_domain.encode())
        self._servers_keys_hash_domain[h] = self._kdc_domain
        self._servers_keys_domain_hash[self._kdc_domain] = h


    def encode(self, domain: str, request: bytes):
        if domain not in self._servers_keys:
            return request

        sig = s2.sign(self._kdc_key)
        data = m1.encrypt(self._domain.encode(), sig, request, self._kdc_key)
        return sig + self._servers_keys_domain_hash[domain] + data
    
    def decode(self, response: bytes):
        if len(response) < 164+64:
            return response
        
        sig, domain_h, data = response[:164], response[164:164+64], response[164+64:]

        if domain_h not in self._servers_keys_hash_domain:
            return response

        key = self._servers_keys[self._servers_keys_hash_domain[domain_h]]
        if not s2.verify(key, sig):
            return None
        return m1.decrypt(self._domain.encode(), sig, data, key)
