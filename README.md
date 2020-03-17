# Python ProtoBuf

This repository is the same representation of the [Java Protobuf example](https://github.com/davidlares/java-protobuf) but with `Python`. On the `simple` package (internal directory) we have the `simple.proto` and the outputted version resulting from the `protoc` compilation process, called `simple_pb2.py` file.

The `simple.py` file is a simple implementation of a `Protobuf Message`, that shows you how can be translated and manipulated with `Python`.

The `protoc` commands used are in the `commands.sh` (root directory)

## Let's recap a bit

The Protocol buffers are a data-type (actually a format) developed by Google used for sharing data across many development languages. This particular data-type is structured and it's defined with the `.proto` file extension, also, is fully typed, very comprehensive but schema-based.

Some databases offer support for `Protobuf` data format, this tool is internally used by Google and a lot of RPC frameworks have a natural adoption in order to exchange data. You can check for more information [here](https://developers.google.com/protocol-buffers/).

## Usage

Set a `virtualenv` environment and handle dependencies with `pip` (check `requirements.txt`)

Then, just: `python simple.py`

## Credits

 [David E Lares](https://twitter.com/davidlares3)

## License

 [MIT](https://opensource.org/licenses/MIT)
