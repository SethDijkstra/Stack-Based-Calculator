package ADTStack;

import java.util.EmptyStackException;

/**
 * An interface for the ADT stack.
 *
 * @param <T> the type of elements in the stack
 */
public interface StackInterface<T> {
    /**
     * Adds a new entry to the top of this stack.
     *
     * @param newEntry the object to be added to the stack
     */
    void push(T newEntry);

    /**
     * Removes and returns this stack's top entry.
     *
     * @return the object at the top of the stack
     * @throws EmptyStackException if the stack is empty before the operation
     */
    T pop() throws EmptyStackException;

    /**
     * Retrieves this stack's top entry.
     *
     * @return the object at the top of the stack
     * @throws EmptyStackException if the stack is empty
     */
    T peek() throws EmptyStackException;

    /**
     * Detects whether this stack is empty.
     *
     * @return true if the stack is empty, false otherwise
     */
    boolean isEmpty();

    /**
     * Removes all entries from this stack.
     */
    void clear();
}//end StackInterface
