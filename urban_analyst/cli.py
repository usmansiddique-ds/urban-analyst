import click 
@click.command()
@click.option('--city', default=None, help='City name e.g."Lahore, Pakistan:"')
@click.option('--bbox', nargs=4 , type=float, default=None, 
              help='Bounding box coordinates: min_lon min_lat max_lon max_lat')
@click.option('--cell-size', default=200, help='Grid cell size in meters')
def main(city, bbox, cell_size):
    """Urban Analyst - GIS Pipeline for Urban Analysis"""
    if city is None and bbox is None:
        click.echo("Error: Please provide --city or --bbox")
        return
    if bbox is not None:
        lon_min, lat_min, lon_max, lat_max = bbox
        click.echo(f"Using bounding box: {bbox}")
    else:
        click.echo(f"Using city: {city}")
    click.echo(f"Using cell size: {cell_size} meters")
    click.echo("Pipeline Started...!")
if __name__ == "__main__":
    main()
