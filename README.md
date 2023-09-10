# This is my package laravel-khmer-slug

> This package is in development.

This is use for simple slug and make url friendly for khmer charter. This package inspire by [khmer-nltk](https://github.com/VietHoang1512/khmer-nltk)

## Installation
> You have to install and configure [bhavingajjar/laravel-python](https://github.com/bhavingajjar/laravel-python) package first before  continue.

You can install the package via composer:

```bash
composer require reaksmey/laravel-khmer-slug
```

You can publish the config file with:

```bash
php artisan vendor:publish --tag="laravel-khmer-slug-config"
```

## Usage

```php
use Reaksmey\KhmerSlug\Facades\KhmerSlug;

$raw_text = "ស្មារតីផ្សះផ្សាជាតិរវាងខ្មែរនិងខ្មែរ ឈានទៅបញ្ចប់សង្រ្គាម នាំពន្លឺសន្តិភាព និងការរួបរួមជាថ្មី";
KhmerSlug::slug($raw_text);

==> "ស្មារតី-ផ្សះផ្សា-ជាតិ-រវាង-ខ្មែរ-និង-ខ្មែរ-ឈាន-ទៅ-បញ្ចប់-សង្រ្គាម-នាំ-ពន្លឺ-សន្តិភាព-និង-ការរួបរួម-ជាថ្មី"
```

## Testing

```bash
composer test
```

## Changelog

Please see [CHANGELOG](CHANGELOG.md) for more information on what has changed recently.

## Contributing

Please see [CONTRIBUTING](CONTRIBUTING.md) for details.

## Security Vulnerabilities

Please review [our security policy](../../security/policy) on how to report security vulnerabilities.

## Credits

- [Reaksmey SERY](https://github.com/Reaksmey)
- [All Contributors](../../contributors)

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
