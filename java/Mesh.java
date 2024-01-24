import java.util.ArrayList;
import java.util.HashMap;

class Point {
	double x;
	double y;

	Point(double x, double y) {
		this.x = x;
		this.y = y;
	}
	
	@Override
	public String toString() {
		return "Point(" + x + ", " + y + ")";
	}
}

class Vertex {
	Point pos;
	Edge edge;

	Vertex(Point pos) {
		this.pos = pos;
	}
	@Override
	public String toString() {
		return pos.toString();
	}
}

class Edge {
	Vertex vertex;
	Face face;
	Edge next;
	Edge prev;
	Edge oppo;

	Edge(Vertex vertex) {
		this.vertex = vertex;
	}
	@Override
	public String toString() {
		return vertex.toString() + " --> " + prev.vertex.toString();
	}
}

class Face {
	Edge edge;

	Face(Edge edge) {
		this.edge = edge;
	}
}

public class Mesh {
	public static void main(String[] args){
		HashMap<String, Point> points = new HashMap<String, Point>();
		points.put("P1", new Point(5.15,  2.65));
		points.put("P2", new Point(1.70,  4.45));
		points.put("P3", new Point(1.65,  8.95));
		points.put("P4", new Point(4.95,  10.5));
		points.put("P5", new Point(7.80,  8.65));
		points.put("P6", new Point(8.15,  4.85));
		points.put("P7", new Point(12.75, 4.50));
		points.put("P8", new Point(11.2,  9.85));
		points.put("P9", new Point(10.8,  0.00));
		points.put("P10",new Point(5.55,  14.85));
		points.forEach((key, value) -> {
			System.out.println(value);
		});
		System.out.println("");

		HashMap<String, Vertex> vertices = new HashMap<String, Vertex>();
		for (int i = 1; i <= points.size(); i++) {
			vertices.put("V" + i, new Vertex(points.get("P" + i)));
		}
		vertices.forEach((key, value) -> {
			System.out.println(value);
		});

		HashMap<String, Edge> edges = new HashMap<String, Edge>();
		for (int i = 1; i < 6; i++) {
			edges.put("E"+i, new Edge(vertices.get("V"+(i+1))));
			vertices.get("V"+i).edge = edges.get("E"+i);
		}
	}
}