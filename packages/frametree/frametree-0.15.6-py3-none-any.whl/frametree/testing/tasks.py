import shutil
from pathlib import Path
import typing as ty
import attrs
from pydra.compose import python, workflow
import fileformats.core
from fileformats.text import TextFile
import fileformats.text
from frametree.core.row import DataRow


@python.define
def Add(a: float, b: float) -> float:
    return a + b


@python.define
def PathManip(dpath: Path, fname: str) -> tuple[str, str]:
    """
    Returns
    -------
    path : str
        extracted path
    suffix : str
        the extracted suffix
    """
    path = dpath / fname
    return str(path), path.suffix


@attrs.define(auto_attribs=True)
class A:
    x: int
    y: int


@attrs.define(auto_attribs=True)
class B:
    u: float
    v: float


@attrs.define(auto_attribs=True)
class C:
    z: float


@python.define
def AttrsFunc(a: A, b: B) -> C:
    """A function that takes two attrs classes and returns a third

    Parameters
    ----------
    a : A
        an attrs class
    b : B
        another attrs class

    Returns
    -------
    c : C
        a third attrs class
    """
    return C(z=a.x * b.u + a.y * b.v)


@python.define(outputs=["out_file"])
def Concatenate(
    in_file1: TextFile,
    in_file2: TextFile,
    duplicates: int = 1,
) -> TextFile:
    """Concatenates the contents of two files and writes them to a third

    Parameters
    ----------
    in_file1 : Path
        A text file
    in_file2 : Path
        Another text file

    Returns
    -------
    out_file: Path
        A text file made by concatenating the two inputs
    """
    out_file = Path("out_file.txt").absolute()
    contents = []
    for _ in range(duplicates):
        for fname in (in_file1, in_file2):
            with open(fname) as f:
                contents.append(f.read())
    with open(out_file, "w") as f:
        f.write("\n".join(contents))
    return out_file


@python.define(outputs=["out_file"])
def Reverse(in_file: TextFile) -> TextFile:
    """Reverses the contents of a file and outputs it to another file

    Parameters
    ----------
    in_file : TextFile
        A text file

    Returns
    -------
    out_file: Path
        A text file with reversed contents to the original
    """
    out_file = Path("out_file.txt").absolute()
    with open(in_file) as f:
        contents = f.read()
    with open(out_file, "w") as f:
        f.write(contents[::-1])
    return out_file


@workflow.define(outputs=["out_file"])
def ConcatenateReverse(
    in_file1: TextFile, in_file2: TextFile, duplicates: int
) -> TextFile:
    """A simple workflow that has the same signature as concatenate, but
    concatenates reversed contents of the input files instead

    Parameters
    ----------
    name : str
        name of the workflow to be created
    **kwargs
        keyword arguments passed through to the workflow init, can be any of
        the workflow's input spec, i.e. ['in_file1', 'in_file2', 'duplicates']

    Returns
    -------
    out_file: TextFile
        The file made by concatenating the reversed contents of the two inputs
    """

    reverse1 = workflow.add(Reverse(in_file=in_file1), name="reverse1")

    reverse2 = workflow.add(Reverse(in_file=in_file2), name="reverse2")

    concatenate = workflow.add(
        Concatenate(
            in_file1=reverse1.out_file,
            in_file2=reverse2.out_file,
            duplicates=duplicates,
        )
    )

    return concatenate.out_file


@python.define
def Plus10ToFilenumbers(filenumber_row: DataRow) -> None:
    """Alters the item paths within the data row, by converting them to
    an int and adding 10. Used in the test_run_pipeline_on_row_cli test.

    Parameters
    ----------
    row : DataRow
        the data row to modify
    """
    for entry in filenumber_row.entries:
        item = fileformats.text.TextFile(ty.cast(fileformats.core.FileSet, entry.item))
        new_item_stem = str(int(item.stem) + 10)
        shutil.move(item.fspath, item.fspath.parent / (new_item_stem + item.actual_ext))


@python.define
def Identity(in_: ty.Any) -> ty.Any:
    return in_


@python.define
def MultiplyContents(
    in_file: TextFile,
    multiplier: ty.Union[int, float],
    out_file: ty.Optional[Path] = None,
    dtype: type = float,
) -> TextFile:
    """Multiplies the contents of the file, assuming that it contains numeric
    values on separate lines

    Parameters
    ----------
    in_file : Path
        path to input file to multiply the contents of
    multiplier : int or float
        the multiplier to apply to the file values
    out_file : Path
        the path to write the output file to
    dtype : type
        the type to cast the file contents to"""

    if out_file is None:
        out_file = Path("out_file.txt").absolute()

    with open(in_file) as f:
        contents = f.read()

    multiplied = []
    for line in contents.splitlines():
        multiplied.append(str(dtype(line.strip()) * multiplier))

    with open(out_file, "w") as f:
        f.write("\n".join(multiplied))

    return TextFile(out_file)


@python.define
def ContentsAreNumeric(in_file: TextFile) -> bool:
    """Checks the contents of a file to see whether each line can be cast to a numeric
    value

    Parameters
    ----------
    in_file : Path
        the path to a text file

    Returns
    -------
    bool
        if all the lines are numeric return True
    """
    with open(in_file) as f:
        contents = f.read()
    try:
        float(contents.strip())
    except ValueError:
        return False
    return True


@python.define
def CheckLicense(
    expected_license_path: TextFile,
    expected_license_contents: TextFile,
) -> TextFile:
    """Checks the `expected_license_path` to see if there is a file with the same contents
    as that of `expected_license_contents`

    Parameters
    ----------
    expected_license_path : File
        path to the expected license file
    expected_license_contents : File
        path containing the contents expected in the expected license file

    Returns
    -------
    File
        passes through the expected license file so the task can be connected back to the
        dataset
    """
    with open(expected_license_contents) as f:
        expected_contents = f.read()
    with open(expected_license_path) as f:
        actual_contents = f.read()
    if expected_contents != actual_contents:
        raise Exception(
            f'License contents "{actual_contents}" did not match '
            f'expected "{expected_contents}"'
        )
    return expected_license_contents


TEST_TASKS = {
    "add": (Add, {"a": 4, "b": 5}, {"out": 9}),
    "path_manip": (
        PathManip,
        {"dpath": Path("/home/foo/Desktop"), "fname": "bar.txt"},
        {"path": "/home/foo/Desktop/bar.txt", "suffix": ".txt"},
    ),
    "attrs_func": (
        AttrsFunc,
        {"a": A(x=2, y=4), "b": B(u=2.5, v=1.25)},
        {"c": C(z=10)},
    ),
}

BASIC_TASKS = ["Add", "PathManip", "AttrsFunc"]

FILE_TASKS = ["Concatenate"]
