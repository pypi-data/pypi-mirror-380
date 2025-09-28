import pytest
from togo import Geometry, Point, Ring, Poly


def test_geometry_wkt():
    g = Geometry("POINT(1 2)", fmt="wkt")
    assert g.type_string() == "Point"
    assert g.rect() == ((1.0, 2.0), (1.0, 2.0))
    assert g.memsize() == 24
    assert g.num_points() == 0  # FIXME? Points in a Point geometry is considered 0
    assert not g.is_feature()
    assert not g.is_featurecollection()
    assert not g.is_empty()
    assert g.dims() == 2
    assert g.has_z() is False
    assert g.has_m() is False
    assert g.to_wkt() == "POINT(1 2)"


def test_geometry_equals():
    g1 = Geometry("POINT(1 2)", fmt="wkt")
    g2 = Geometry("POINT(1 2)", fmt="wkt")
    g3 = Geometry("POINT(2 3)", fmt="wkt")
    assert g1.equals(g2)
    assert not g1.equals(g3)


def test_geometry_disjoint():
    g1 = Geometry("POINT(1 2)", fmt="wkt")
    g2 = Geometry("POINT(2 3)", fmt="wkt")
    assert g1.disjoint(g2)


def test_geometry_contains():
    g1 = Geometry("POINT(1 2)", fmt="wkt")
    g2 = Geometry("POINT(1 2)", fmt="wkt")
    assert g1.contains(g2)


def test_geometry_to_geojson():
    g = Geometry("POINT(1 2)", fmt="wkt")
    geojson = g.to_geojson()
    assert geojson == '{"type":"Point","coordinates":[1,2]}'


def test_geometry_to_hex():
    g = Geometry("POINT(1 2)", fmt="wkt")
    hexstr = g.to_hex()
    assert hexstr == "0101000000000000000000F03F0000000000000040"


def test_geometry_to_wkb():
    g = Geometry("POINT(1 2)", fmt="wkt")
    wkb = g.to_wkb()
    assert (
        wkb
        == b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@"
    )


def test_geometry_to_geobin():
    g = Geometry("POINT(1 2)", fmt="wkt")
    geobin = g.to_geobin()
    assert (
        geobin
        == b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@"
    )


def test_geometry_intersects():
    g1 = Geometry("POLYGON((10 10,20 10,20 20,10 20,10 10))", fmt="wkt")
    g2 = Geometry("POINT(15 15)", fmt="wkt")
    g3 = Geometry("POINT(23 24)", fmt="wkt")
    assert g1.intersects(g2)
    assert not g1.intersects(g3)


def test_equals():
    g1 = Geometry("POINT(1 2)", fmt="wkt")
    g2 = Geometry('{"type":"Point","coordinates":[1,2]}', fmt="geojson")
    g3 = Geometry("POINT(2 3)", fmt="wkt")
    assert g1.equals(g2)
    assert not g1.equals(g3)


def test_geometry_num_lines_polys_geometries():
    g_lines = Geometry("MULTILINESTRING((0 0,1 1),(2 2,3 3))", fmt="wkt")
    assert g_lines.num_lines() == 2
    g_polys = Geometry(
        "MULTIPOLYGON(((0 0,1 0,1 1,0 1,0 0)),((2 2,3 2,3 3,2 3,2 2)))", fmt="wkt"
    )
    assert g_polys.num_polys() == 2
    g_collection = Geometry(
        "GEOMETRYCOLLECTION(POINT(1 2),LINESTRING(0 0,1 1))", fmt="wkt"
    )
    assert g_collection.num_geometries() == 2
    # Use Geometry.__getitem__ to access sub-geometries of MultiLineString
    first_line = g_lines[0]
    assert first_line.type_string() == "LineString"


def test_geometry_z_m():
    g = Geometry("POINT ZM (1 2 3 4)", fmt="wkt")
    assert g.has_z() is True
    assert g.has_m() is True
    assert g.z() == 3.0
    assert g.m() == 4.0


def test_geometry_spatial_predicates():
    g1 = Geometry("POLYGON((0 0,2 0,2 2,0 2,0 0))", fmt="wkt")
    g2 = Geometry("POINT(1 1)", fmt="wkt")
    g3 = Geometry("POINT(3 3)", fmt="wkt")
    assert g1.covers(g2)
    assert g2.coveredby(g1)
    assert not g1.covers(g3)
    assert not g3.coveredby(g1)
    assert g1.touches(Geometry("LINESTRING(0 0,2 0)", fmt="wkt"))
    assert g1.intersects(g2)
    assert not g1.intersects(g3)


def test_geometry_to_wkb_and_geobin():
    g = Geometry("POINT(1 2)", fmt="wkt")
    wkb = g.to_wkb()
    geobin = g.to_geobin()
    assert isinstance(wkb, bytes)
    assert isinstance(geobin, bytes)
    assert len(wkb) > 0
    assert len(geobin) > 0


def test_geometry_constructor_wkt():
    g = Geometry("POINT(1 2)", fmt="wkt")
    assert g.type_string() == "Point"
    assert g.rect() == ((1.0, 2.0), (1.0, 2.0))


def test_geometry_constructor_geojson():
    geojson = '{"type":"Point","coordinates":[1,2]}'
    g = Geometry(geojson, fmt="geojson")
    assert g.type_string() == "Point"
    assert g.rect() == ((1.0, 2.0), (1.0, 2.0))


def test_geometry_constructor_hex():
    hexstr = "0101000000000000000000F03F0000000000000040"
    g = Geometry(hexstr, fmt="hex")
    assert g.type_string() == "Point"
    assert g.rect() == ((1.0, 2.0), (1.0, 2.0))


def test_geometry_constructor_invalid():
    # Note: The Geometry constructor only supports 'wkt', 'geojson', and 'hex' formats.
    # 'wkb' is not a supported input format for the constructor.
    with pytest.raises(ValueError):
        Geometry("not a geometry", fmt="wkt")
    with pytest.raises(ValueError):
        Geometry("not a geometry", fmt="geojson")
    with pytest.raises(ValueError):
        Geometry("not a geometry", fmt="hex")


def test_geometry_point_accessor():
    g = Geometry("POINT(3 4)", fmt="wkt")
    pt = g.point()
    assert pt.x == 3.0 and pt.y == 4.0


def test_geometry_line_accessor_and_from_linestring():
    points = [(0, 0), (1, 1), (2, 2)]
    g = Geometry.from_linestring(points)
    line = g.line()
    pts = line.points()
    assert pts == points


def test_geometry_poly_accessor():
    # Polygon with one ring
    wkt = "POLYGON((0 0,1 0,1 1,0 1,0 0))"
    g = Geometry(wkt, fmt="wkt")
    poly = g.poly()
    ext = poly.exterior()
    assert ext.num_points() == 5


def test_geometry_geom_at():
    # GeometryCollection with two points
    g = Geometry("GEOMETRYCOLLECTION(POINT(1 2),POINT(3 4))", fmt="wkt")
    g0 = g[0]
    g1 = g[1]
    assert g0.type_string() == "Point"
    assert g1.type_string() == "Point"
    assert g0.point().x == 1.0 and g0.point().y == 2.0
    assert g1.point().x == 3.0 and g1.point().y == 4.0


def test_tgx_meters_grid():
    # Create a simple point geometry
    g = Geometry('{"type": "Point", "coordinates": [1.0, 2.0]}')
    origin = Point(0.0, 0.0)
    g2 = g.to_meters_grid(origin)
    g3 = g2.from_meters_grid(origin)
    # Should round-trip back to original coordinates
    assert g3.point().x == pytest.approx(1.0, abs=1e-6)
    assert g3.point().y == pytest.approx(2.0, abs=1e-6)


def test_unary_union_geos_lines():
    g1 = Geometry("LINESTRING(0 0, 1 1)", fmt="wkt")
    g2 = Geometry("LINESTRING(1 1, 2 2)", fmt="wkt")
    u = Geometry.unary_union([g1, g2])
    assert u.type_string() == "MultiLineString"
    wkt = u.to_wkt()
    assert wkt == "MULTILINESTRING((0 0,1 1),(1 1,2 2))"


def test_unary_union_geos_polys():
    # Two intersecting squares
    outer1 = Ring([(0, 0), (2, 0), (2, 2), (0, 2), (0, 0)])
    poly1 = Poly(outer1)
    outer2 = Ring([(1, 1), (3, 1), (3, 3), (1, 3), (1, 1)])
    poly2 = Poly(outer2)
    union_geom = Geometry.unary_union([poly1, poly2])
    # Should be a single Polygon
    assert union_geom.type_string() == "Polygon"
    # Area should be 7 (each square is 4, overlap is 1)
    # So union area = 4 + 4 - 1 = 7
    area = union_geom.poly().exterior().area()
    assert area == 7.0
    # Bounding box should be ((0,0),(3,3))
    assert union_geom.rect() == ((0.0, 0.0), (3.0, 3.0))
    # WKT should represent the merged polygon
    wkt = union_geom.to_wkt()
    assert wkt == "POLYGON((2 0,0 0,0 2,1 2,1 3,3 3,3 1,2 1,2 0))"
