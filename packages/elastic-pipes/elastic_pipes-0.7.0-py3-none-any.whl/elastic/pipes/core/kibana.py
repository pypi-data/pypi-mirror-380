# Copyright 2025 Elasticsearch B.V.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Helper class for accessing the Kibana REST API."""

import json
import uuid

import requests


class Kibana:
    """Minimal (unofficial) Kibana REST API Python client"""

    exceptions = requests.exceptions

    def __init__(self, url=None, cloud_id=None, basic_auth=None, api_key=None, verify_certs=True, ca_certs=None):
        if not (url or cloud_id):
            raise ValueError("Either `url` or `cloud_id` must be defined")

        self.url = url
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json", "kbn-xsrf": str(uuid.uuid4())})

        if api_key:
            self.session.headers["Authorization"] = f"ApiKey {api_key}"
        if basic_auth:
            self.session.auth = requests.auth.HTTPBasicAuth(*basic_auth)
        if not verify_certs:
            self.session.verify = False
        elif ca_certs:
            self.session.verify = ca_certs

        retry_strategy = requests.packages.urllib3.util.retry.Retry(
            total=3,
            allowed_methods=["HEAD", "GET", "OPTIONS"],
        )

        adapter = requests.adapters.HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

        if cloud_id:
            import base64

            cluster_name, cloud_info = cloud_id.split(":")
            domain, es_uuid, kibana_uuid = base64.b64decode(cloud_info.encode("utf-8")).decode("utf-8").split("$")

            if domain.endswith(":443"):
                domain = domain[:-4]

            url_from_cloud = f"https://{kibana_uuid}.{domain}:9243"
            if self.url and self.url != url_from_cloud:
                raise ValueError(f"url provided ({self.url}) does not match url derived from cloud_id {url_from_cloud}")
            self.url = url_from_cloud

    def close(self):
        self.session.close()

    def ping(self):
        try:
            self.status()
            return True
        except requests.exceptions.ConnectionError:
            return False

    def status(self):
        url = f"{self.url}/api/status"
        res = self.session.get(url)
        res.raise_for_status()
        return res.json()

    def create_siem_index(self):
        url = f"{self.url}/api/detection_engine/index"
        res = self.session.post(url)
        res.raise_for_status()
        return res.json()

    def get_siem_index(self):
        url = f"{self.url}/api/detection_engine/index"
        res = self.session.get(url)
        res.raise_for_status()
        return res.json()

    def create_detection_engine_rule(self, rule):
        url = f"{self.url}/api/detection_engine/rules"
        res = self.session.post(url, data=json.dumps(rule))
        res.raise_for_status()
        return res.json()

    def get_detection_engine_rule(self, rule):
        url = f"{self.url}/api/detection_engine/rules?id={rule['id']}"
        res = self.session.get(url, data=json.dumps(rule))
        res.raise_for_status()
        return res.json()

    def delete_detection_engine_rule(self, rule):
        url = f"{self.url}/api/detection_engine/rules?id={rule['id']}"
        res = self.session.delete(url)
        res.raise_for_status()
        return res.json()

    def find_detection_engine_rules(self, count_max, enabled=None):
        count_max += 1
        url = f"{self.url}/api/detection_engine/rules/_find?per_page={count_max}"
        if enabled is not None:
            url += f"&filter=alert.attributes.enabled:{str(enabled).lower()}"
        res = self.session.get(url)
        res.raise_for_status()
        rules = res.json()["data"]
        if len(rules) == count_max:
            raise ValueError(f"The number of returned rules is suspiciously equal to count_max ({count_max})")
        return rules

    def create_detection_engine_rules(self, rules):
        body = "\n".join(json.dumps(rule) for rule in rules)
        files = {"file": ("rules.ndjson", body, "application/octet-stream")}
        url = f"{self.url}/api/detection_engine/rules/_import"
        res = self.session.post(url, files=files, headers={"Content-Type": None})
        res.raise_for_status()
        ret = res.json()
        if ret["errors"]:
            raise ValueError("Could not create rule(s):\n  " + "\n  ".join(str(x) for x in ret["errors"]))
        return ret

    def delete_all_detection_engine_rules(self):
        url = f"{self.url}/api/detection_engine/rules/_bulk_action"
        req = {"action": "delete", "query": ""}
        res = self.session.post(url, data=json.dumps(req))
        res.raise_for_status()

    def search_detection_engine_signals(self, body):
        url = f"{self.url}/api/detection_engine/signals/search"
        res = self.session.post(url, data=json.dumps(body))
        res.raise_for_status()
        return res.json()
