import "@typespec/http";
import "@typespec/rest";

using TypeSpec.Http;
using TypeSpec.Rest;

@service(#{
  title: "Library Management",
})
@server("http://localhost:8080/api/v1", "Local development server")
namespace LibraryManagement;

// Models

model BookDetails {
  bookId?: string;
  title: string;
  author: string;
  publishYear: int32;
}

model BookListResponse {
  books: BookDetails[];
}

// Routes

@route("/books")
interface Books {

  /**
   * Get list of books
   */
  @get
  listBooks(
    @query title?: string,
    @query author?: string
  ): BookListResponse | Error500;

  /**
   * Create a book resource
   */
  @post
  createBook(
    @body body: BookDetails
  ): CreatedResponse | BadRequest | Error500;
}

@route("/books/{bookId}")
interface BookById {

  /**
   * Get Book by Id
   */
  @get
  getBookById(
    @path bookId: string
  ): BookDetails | BadRequest | NotFound | Error500;

  /**
   * Update Book by Id
   */
  @put
  updateBookById(
    @path bookId: string,
    @body body: BookDetails
  ): BookDetails | BadRequest | NotFound | Error500;

  /**
   * Delete Book by Id
   */
  @delete
  deleteBookById(
    @path bookId: string
  ): BookDetails | BadRequest | NotFound | Error500;
}

// Response Models

@error
model BadRequest {
  @statusCode statusCode: 400;
}

@error
model NotFound {
  @statusCode statusCode: 404;
}

@error
model Error500 {
  @statusCode statusCode: 500;
}

model CreatedResponse {
  @statusCode statusCode: 201;
}