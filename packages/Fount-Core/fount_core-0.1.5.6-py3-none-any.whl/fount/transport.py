from __future__ import annotations
from typing import Optional
from io import BytesIO
import json
import csv
import openpyxl
import sys
import httpx
import logging
from ._exceptions import TrainingError, UnauthorizedError, TimedOutError, RequestError, EntityError

logger = logging.getLogger(__name__)


class HTTPTransport:
    def __init__(
        self,
        base_url: httpx.URL | str,
        timeout: float,
        api_key: str,
        client: Optional[httpx.Client] = None,
    ):
        self.client = client or httpx.Client(
            base_url=base_url,
            timeout=timeout,
            headers={"X-API-Key": f"{api_key}"} if api_key else {},
        )

    def upload_dataframe(self, dataframe, name):
        csv_params = {"index": False, "encoding": "utf-8", "compression": None}
        buffer = BytesIO()
        try:
            dataframe.to_csv(buffer, **csv_params)
            files = {"file": ("dataframe.csv", buffer.getvalue(), "text/csv")}
            try:
                job_id = None
                sys.stdout.write("==> Preparing for upload\n")
                with self.client.stream(
                    method="POST",
                    params={"name": name},
                    url="upload",
                    files=files,
                ) as _stream_response:
                    _stream_response.raise_for_status()
                    for chunk in _stream_response.iter_text():
                        try:
                            data = json.loads(chunk)
                        except json.JSONDecodeError:
                            continue
                        sys.stdout.write(f"\r{data.get('status')}")
                        sys.stdout.flush()
                        if "job_id" in data:
                            job_id = data.get("job_id")
                return job_id
            except httpx.TimeoutException:
                raise TimedOutError("Request timed out")
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 401:
                    raise UnauthorizedError("Check API key or credentials") from e
                elif e.response.status_code == 422:
                    raise EntityError("Params error") from e
            except httpx.RequestError as e:
                logger.error(
                    f"\nAn error occurred while requesting {e.request.url!r}: {e}"
                )
                raise RequestError("Request error") from e
        finally:
            buffer.close()

    def upload_csv(self, pathname, name):
        with open(pathname, "r") as file:
            reader = csv.reader(file)
            buffer = BytesIO()
            writer = csv.writer(buffer)
            for row in reader:
                writer.writerow(row)
        files = {"file": ("dataframe.csv", buffer.getvalue(), "text/csv")}
        return self.client.post("upload", files=files, params={"name": name})

    def upload_excel(self, pathname, sheet_name, name):
        buffer = BytesIO()
        workbook = openpyxl.load_workbook(buffer, pathname)
        if sheet_name:
            if sheet_name not in workbook.sheetnames:
                raise ValueError(f"Sheet {sheet_name} not found in {pathname}")
            sheet = workbook[sheet_name]
        else:
            sheet = workbook.active
        buffer = BytesIO()

        buffer.seek(0)
        files = {
            "file": (
                "dataframe.xlsx",
                buffer.getvalue(),
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
        }
        return self.client.post("upload", files=files, params={"name": name})

    def start_job(self, job_type, payload):
        try:
            _r = self.client.post(job_type, json=payload)
            if _r.is_success:
                return _r.json()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 422:
                raise TrainingError("Unprocessable entity")
            elif e.response.status_code == 500:
                raise TrainingError("Something went wrong")

    def get_model(self, _p):
        req = self.client.get("model", params={"type": _p})
        return req.json()

    def get_job_status(self, _p):
        req = self.client.get("status", params={"task_id": _p})
        return req.json()

    def get_job_metrics(self, _p):
        return self.client.get("metrics", params={"task_id": _p}).json()

    def get_artifacts(self, _p):
        return self.client.get("metrics", params={"task_id": _p}).json()

    # def stream_events(self,job_type,id):
    #     ...

    def close(self):
        return None
