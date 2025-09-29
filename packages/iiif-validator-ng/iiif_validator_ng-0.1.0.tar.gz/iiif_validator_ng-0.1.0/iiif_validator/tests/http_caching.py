from typing import Literal
from urllib.request import Request

from .test import (
    ValidationTest,
    ComplianceLevel,
    TestCategory,
    IIIFVersion,
    TargetServer,
    ValidationFailure,
    ValidationSuccess,
    make_request,
    ImageAPIRequest,
)


class HttpCachingTest(ValidationTest):
    name = "Proper HTTP Caching implementation for info.json and images"
    compliance_level = ComplianceLevel.OPTIONAL
    category = TestCategory.HTTP
    versions = [IIIFVersion.V2, IIIFVersion.V3]

    @staticmethod
    def run(server: TargetServer) -> list[ValidationSuccess | ValidationFailure]:
        results = []
        for resource_type in ("info", "image"):
            results.extend(_single_run(server, resource_type))
        return results


def _single_run(
    server: TargetServer,
    resource_type: Literal["info", "image"],
) -> list[ValidationSuccess | ValidationFailure]:
    results = []
    etag = None
    last_modified = None
    if resource_type == "info":
        url = server.info_url()
    else:
        url = ImageAPIRequest.of().url(server)
    for method in ("HEAD", "GET"):
        resp = make_request(Request(url, method=method))
        etag = resp.headers.get("etag", None)
        if etag is not None:
            results.append(
                ValidationSuccess(
                    details=f"ETag header on {resource_type} with method={method} present"
                )
            )
            continue
        last_modified = resp.headers.get("last-modified", None)
        if last_modified is not None:
            results.append(
                ValidationSuccess(
                    details=f"Last-Modified header on {resource_type} with method={method} present"
                )
            )
            continue
        results.append(
            ValidationFailure(
                url=url,
                expected="Either ETag or Last-Modified header",
                received="Neither ETag nor Last-Modified header",
                details=f"Server did not provide any caching headers on {resource_type} with method={method}",
            )
        )
    extra_headers = {}
    if etag is not None:
        extra_headers["If-None-Match"] = etag
    if last_modified is not None:
        extra_headers["If-Modified-Since"] = last_modified
    else:
        return results

    resp = make_request(url, extra_headers=extra_headers)
    if resp.status == 304:
        results.append(
            ValidationSuccess(
                details=f"Server returned HTTP 304 Not Modified for a conditional request on the validation {resource_type}"
            )
        )
    else:
        results.append(
            ValidationFailure(
                url=url,
                expected="304 Not Modified",
                received=f"{resp.status} {resp.body.decode('utf-8', errors='replace')}",
                details=f"Server did not return the expected response on the validation {resource_type}.",
            )
        )
    return results
