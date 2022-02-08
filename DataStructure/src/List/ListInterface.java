package List;

public interface ListInterface<T> {
	boolean add (T value);
	void add (int index, T value);
	T remove (int value);
	void set (int index, T value);
	void clear();
	boolean contains (Object value);
	int indexOf (Object value);
	T get (int index);
	int size();
	void dump();
	void sort();
	Object[] toArray();

}
