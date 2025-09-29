# PGPack format

Storage format for PGCopy dump packed into LZ4, ZSTD or uncompressed with meta data information packed into zlib

## PGPack structure

- header b"PGPACK\n\x00" 8 bytes
- unsigned long integer zlib.crc32 for packed metadata 4 bytes
- unsigned long integer zlib packed metadata length 4 bytes
- zlib packed metadata
- unsigned char compression method 1 byte
- unsigned long long integer packed pgcopy data length 8 bytes
- unsigned long long integer unpacked pgcopy data length 8 bytes
- packed pgcopy data

## Installation

### From pip

```bash
pip install pgpack
```

### From local directory

```bash
pip install .
```

### From git

```bash
pip install git+https://github.com/0xMihalich/pgpack
```

## Metadata format

Metadata for PGCopy dump contained Column names and OID Types

### Decompressed metadata structure

```
list[
    list[
        column number int,
        list[
            column name str,
            column oid int,
            column lengths int,
            column scale int,
            column nested int,
        ]
    ]
]
```

## Compression methods

- NONE (value = 0x02) PGCopy dump without compression
- LZ4 (value = 0x82) PGCopy dump with lz4 compression
- ZSTD (value = 0x90) PGCopy dump with zstd compression

### Get ENUM for set compression method

```python
from pgpack import CompressionMethod

compression_method = CompressionMethod.NONE  # no compression
compression_method = CompressionMethod.LZ4  # lz4 compression (default)
compression_method = CompressionMethod.ZSTD  # zstd compression
```

## Class PGPackReader

Initialization parameters

- fileobj - BufferedReader object (file, BytesIO e t.c)

Methods and attributes

- columns - List columns names
- pgtypes - List PGOid for all columns
- pgparam - List PGParam for all columns
- pgcopy - PGCopy object
- header - b"PGPack\n" 8 bytes
- metadata_crc - integer crc32 sign for metadata_zlib object
- metadata_length - integer length metadata_zlib in bytes
- metadata_zlib - zlib packed metadata in bytes
- compression_method - CompressionMethod object
- pgcopy_compressed_length - integer packed pgcopy data length
- pgcopy_data_length - integer unpacked pgcopy data length
- offset_opener - OffsetOpener object
- pgcopy_compressor - File object for reading uncompressed PGCopy data
- to_bytes() - Method for reading uncompressed PGCopy data as bytes
- to_python() - Method for reading uncompressed PGCopy data as list of python objects
- to_pandas() - Method for reading uncompressed PGCopy data as pandas.DataFrame
- to_polars() - Method for reading uncompressed PGCopy data as polars.DataFrame

## Class PGPackWriter

Initialization parameters

- fileobj - BufferedReader object (file, BytesIO e t.c)
- compression_method - CompressionMethod object (default is CompressionMethod.LZ4)

Methods and attributes

- columns - List columns names
- pgtypes - List PGOid for all columns
- pgparam - List PGParam for all columns
- metadata_end - Integer, zlib packed metadata end position
- fileobj_end - Integer, packed pgcopy data end position
- pgcopy_compressed_length - integer packed pgcopy data length
- pgcopy_data_length - integer unpacked pgcopy data length
- write_metadata(metadata) - Make first blocks with metadata. Parameter: metadata as bytes
- write_pgcopy(pgcopy) - Make second blocks with pgcopy. Parameter: pgcopy as BufferedReader
- write(metadata, pgcopy) - Write PGPack file. Parameters: metadata as bytes, pgcopy as BufferedReader
- from_python(dtype_data) - Write PGPack file from python objects. Parameter: dtype_data as python object list
- from_pandas(data_frame) - Write PGPack file from pandas.DataFrame. Parameter: data_frame as pandas.DataFrame
- from_polars(data_frame) - Write PGPack file from polars.DataFrame. Parameter: data_frame as polars.DataFrame

## Errors

- PGPackError - Base PGPack error
- PGPackHeaderError - Error header signature
- PGPackMetadataCrcError - Error metadata crc32
- PGPackModeError - Error fileobject mode
