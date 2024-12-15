# py command
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
print(book)
# Expected outcome <Book: "Nineteen Eighty-Four">
