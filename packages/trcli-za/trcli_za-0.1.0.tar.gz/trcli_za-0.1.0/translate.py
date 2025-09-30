import click
from googletrans import Translator

@click.command()
@click.argument("text")
@click.argument("dest_lang")
def main(text, dest_lang):
    """Metni başka bir dile çevirir. Örnek: translate "hello" tr"""
    translator = Translator()
    result = translator.translate(text, dest=dest_lang)
    click.echo(f"{text} -> {result.text}")
