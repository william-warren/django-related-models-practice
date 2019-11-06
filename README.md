# Django Related Models Practice

In this assignment you have been given a mostly complete Django Project.
The frontend for the application has been provided for you.
The only thing missing is:

- the Models
- the URLs
- the Views

More specifically...

## Models

This project represents a music database and has 2 models:

- `Album`
- `Song`

### `Album`

`Album` has two fields: `title` and an `artist_name`.

### `Song`

`Song` has three fields: `title`, `seconds`, and `album`.

`Song` should also provide a method `formatted_duration`.
It should return a string that returns `seconds` in `M:SS` format.
Tests have been provided to help you make sure you have a correct
implementation.

## URLs

- `""` should take you to a view named `"album_list"`
- `"album/<id>"` should take you to a view named `"album_detail"`
- `"album/<id>/songs"` should take you to a view named `"new_song"`

## Views

- The `album_list` view should render `"album_list.html"` and provide
  all `Album`s to the context using the key `"albums"`
- The `album_detail` view should use the id provided through the path
  to get the appropriate `Album` from the database and render the
  `"album_detail.html"` template with that `Album` provided in the
  context using the key `album`
- The `new_song` view should (on POST) create a new `Song` in the database
  using the title provided in the POST body, the seconds provided in the POST
  body, and the album id provided in the path.
  It should redirect to `album_detail` for the album id provided in the path.
