import pytest

from microcosmClient.microcosm import AsyncMicrocosmClient


@pytest.mark.asyncio
async def test_links():
    client = AsyncMicrocosmClient()
    uri = "at://did:plc:vc7f4oafdgxsihk4cry2xpze/app.bsky.feed.post/3lgwdn7vd722r"
    nsid = "app.bsky.feed.like"
    result = await client.links(uri, nsid, ".subject.uri")
    await client.close()

    assert isinstance(result, dict)
    assert "linking_records" in result
    assert isinstance(result["linking_records"], list)
    assert "total" in result
    assert isinstance(result["total"], int)


@pytest.mark.asyncio
async def test_links_distinct_dids():
    client = AsyncMicrocosmClient()
    uri = "at://did:plc:vc7f4oafdgxsihk4cry2xpze/app.bsky.feed.post/3lgwdn7vd722r"
    nsid = "app.bsky.feed.like"
    result = await client.links_distinct_dids(uri, nsid, ".subject.uri")
    await client.close()

    assert isinstance(result, dict)
    assert "linking_dids" in result
    assert isinstance(result["linking_dids"], list)
    assert "total" in result
    assert isinstance(result["total"], int)


@pytest.mark.asyncio
async def test_links_count():
    client = AsyncMicrocosmClient()
    target = "did:plc:vc7f4oafdgxsihk4cry2xpze"
    collection = "app.bsky.graph.block"
    result = await client.links_count(target, collection, ".subject")
    await client.close()

    assert isinstance(result, dict)
    assert "total" in result
    assert isinstance(result["total"], int)


@pytest.mark.asyncio
async def test_links_count_distinct_dids():
    client = AsyncMicrocosmClient()
    target = "did:plc:vc7f4oafdgxsihk4cry2xpze"
    collection = "app.bsky.graph.block"
    result = await client.links_count_distinct_dids(target, collection, ".subject")
    await client.close()

    assert isinstance(result, dict)
    assert "total" in result
    assert isinstance(result["total"], int)


@pytest.mark.asyncio
async def test_links_all():
    client = AsyncMicrocosmClient()
    target = "did:plc:oky5czdrnfjpqslsw2a5iclo"
    result = await client.links_all(target)
    await client.close()

    assert isinstance(result, dict)
    assert all(isinstance(v, dict) for v in result.values())


@pytest.mark.asyncio
async def test_links_all_count():
    client = AsyncMicrocosmClient()
    target = "did:plc:oky5czdrnfjpqslsw2a5iclo"
    result = await client.links_all_count(target)
    await client.close()

    assert isinstance(result, dict)
    assert "links" in result
    assert isinstance(result["links"], dict)
