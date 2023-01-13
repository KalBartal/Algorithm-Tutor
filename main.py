# The following code is a Python program that uses the Tkinter library to create a graphical user interface (GUI) for
# displaying information about different sorting algorithms. The program includes a dropdown menu that allows the
# user to select a specific algorithm, and a text box that displays an explanation of the selected algorithm,
# along with its time complexity and best/worst case scenarios.
#
# When the user clicks the "select" button, the program activates a function called "show_algo" which is responsible
# for determining which algorithm has been selected and displaying the corresponding information in the text box.
#
# To create the GUI, the program imports the necessary modules (tkinter and ttk), defines the "show_algo" function,
# and then creates the window, label, dropdown menu, text box and button elements. The "show_algo" function is then
# bound to the "select" button, so that it is executed whenever the button is clicked. The overall program runs as an
# event-driven application, meaning it will respond to user input (clicking the button) to perform specific actions.

import tkinter as tk
from tkinter import ttk


def show_algo(event):
    text_box.delete('1.0', tk.END)
    selection = combo.get()
    if selection == "Bubble Sort":
        text_box.insert(tk.END,
                        "Bubble Sort is a simple sorting algorithm that repeatedly compares adjacent elements and "
                        "swaps them if they are in the wrong order. This continues until the entire list is "
                        "sorted.\n\nThe time complexity for this algorithm is O(n^2).\n\nThe best case scenario is if "
                        "the list is already sorted, in which case the algorithm exits after one pass, while the worst "
                        "case is when the list is in reverse order, in which case it requires n passes.")
    elif selection == "Quick Sort":
        text_box.insert(tk.END,
                        "Quick Sort is a sorting algorithm that uses the partition algorithm in order to divide and "
                        "conquer the list. It selects an element called a pivot and rearranges the array in such a way "
                        "that all elements less than the pivot are placed before the pivot while all elements greater "
                        "than the pivot are placed after the pivot.\n\nThe time complexity for this algorithm is O("
                        "nlog(n)).\n\nThe best case scenario is when the pivot divides the array into equal halves, "
                        "while the worst case is when the pivot is always the smallest or largest element in the "
                        "array.")
    elif selection == "Merge Sort":
        text_box.insert(tk.END,
                        "Merge Sort is a sorting algorithm that uses the divide and conquer strategy. It divides the "
                        "list into equal halves and then merges them in the correct order.\n\nThe time complexity for "
                        "this algorithm is O(nlog(n)).\n\nThe best case scenario is when the list is already sorted, "
                        "in which case it requires no comparisons, while the worst case is when the list is reverse "
                        "sorted, in which case it requires nlog(n) comparisons.")
    elif selection == "Selection Sort":
        text_box.insert(tk.END,
                        "Selection Sort is a sorting algorithm that iterates through the list and finds the smallest "
                        "element and swaps it with the first element. This process is repeated until the list is "
                        "sorted.\n\nThe time complexity for this algorithm is O(n^2).\n\nThe best case and worst case "
                        "scenarios both require n^2 comparisons.")
    elif selection == "Insertion Sort":
        text_box.insert(tk.END,
                        "Insertion Sort is a sorting algorithm that starts with a single element in the list and then "
                        "continually inserts each remaining element into its correct location.\n\nThe time complexity "
                        "for this algorithm is O(n^2).\n\nThe best case scenario is when the list is already sorted, "
                        "in which case it requires no comparisons, while the worst case is when the list is reverse "
                        "sorted, in which case it requires n^2 comparisons.")
    elif selection == "Heap Sort":
        text_box.insert(tk.END,
                        "Heap Sort is a sorting algorithm that utilizes heaps (specialized data structures) in order "
                        "to sort the array. It starts by building a heap and then repeatedly removes the max element "
                        "and inserts it into the sorted list.\n\nThe time complexity for this algorithm is O(nlog("
                        "n)).\n\nThe best case and worst case scenarios both require nlog(n) comparisons.")
    elif selection == "Shell Sort":
        text_box.insert(tk.END,
                        "Shell Sort is a sorting algorithm that uses the insertion sort algorithm, but divides the "
                        "list into smaller lists and then rearranges them in order to minimize the number of "
                        "comparisons.\n\nThe time complexity for this algorithm is O(n^2).\n\nThe best case and worst "
                        "case scenarios both require n^2 comparisons.")
    elif selection == "Radix Sort":
        text_box.insert(tk.END,
                        "Radix Sort is a sorting algorithm that sorts based on the position of the elements. It "
                        "iteratively sorts the list in order to place the elements in the correct order.\n\nThe time "
                        "complexity for this algorithm is O(nlog(n)).\n\nThe best case scenario is when the list is "
                        "already sorted, in which case it requires no comparisons, while the worst case is when the "
                        "list is reverse sorted, in which case it requires nlog(n) comparisons.")
    elif selection == "Counting Sort":
        text_box.insert(tk.END,
                        "Counting Sort is a sorting algorithm that uses the counting principle in order to sort the "
                        "list. It works by counting the number of elements at each value and then building a sorted "
                        "list from that data.\n\nThe time complexity for this algorithm is O(n+k) where k is the "
                        "largest element in the list.\n\nThe best case and worst case scenarios both require n+k "
                        "comparisons.")
    elif selection == "Bucket Sort":
        text_box.insert(tk.END,
                        "Bucket Sort is a sorting algorithm that uses buckets to store elements based on their "
                        "values. It then sorts each bucket separately before merging them together.\n\nThe time "
                        "complexity for this algorithm is O(n+k) where k is the number of buckets.\n\nThe best case "
                        "and worst case scenarios both require n+k comparisons.")


window = tk.Tk()
window.title("Algorithm Tutor")
window.configure(background="#192812")

# label
label_1 = ttk.Label(window, text="Select an Algorithm:", background="#495E54")
label_1.grid(row=0, column=0, padx=5, pady=5)

# dropdown list
combo = ttk.Combobox(window)
combo['values'] = ("Bubble Sort", "Quick Sort", "Merge Sort", "Selection Sort", "Insertion Sort",
                   "Heap Sort", "Shell Sort", "Radix Sort", "Counting Sort", "Bucket Sort")
combo.grid(row=0, column=1, padx=5, pady=5)
combo.current(0)

# text_box
text_box = tk.Text(window, height=10, width=60, padx=10, pady=10, wrap=tk.WORD)
text_box.grid(row=2, column=0, columnspan=2)
text_box.configure(background="#C5D2FC", foreground="#99ACD2", relief="solid", bd=2, highlightbackground="#6F8792")
text_box.configure(background="#C5D2FC", foreground="#000000", relief="solid", bd=2, highlightbackground="#6F8792")

# button
button = ttk.Button(window, text="Select")
button.grid(row=1, column=1, padx=5, pady=5)
button.bind("<Button-1>", show_algo)

window.mainloop()
