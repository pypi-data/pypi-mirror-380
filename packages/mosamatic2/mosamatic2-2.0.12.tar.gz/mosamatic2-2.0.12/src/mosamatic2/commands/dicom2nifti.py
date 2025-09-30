import click

from mosamatic2.core.tasks import Dicom2NiftiTask


@click.command(help='Converts root directory with DICOM series to NIFTI format')
@click.option(
    '--scans', 
    required=True, 
    type=click.Path(exists=True), 
    help='Root directory with DICOM scans (one for each patient)',
)
@click.option(
    '--output', 
    required=True, 
    type=click.Path(), 
    help='Output directory'
)
@click.option(
    '--overwrite', 
    type=click.BOOL, 
    default=False, 
    help='Overwrite [true|false]'
)
def dicom2nifti(scans, output, overwrite):
    """
    Converts DICOM scans to NIFTI format.
    
    Parameters
    ----------
    --scans : str
        Root directory with DICOM scans (one subdirectory for each patient)

    --output : str
        Path to output directory

    --overwrite : bool
        Overwrite contents output directory [true|false]
    """
    task = Dicom2NiftiTask(
        inputs={'scans': scans},
        params=None,
        output=output,
        overwrite=overwrite,
    )
    task.run()