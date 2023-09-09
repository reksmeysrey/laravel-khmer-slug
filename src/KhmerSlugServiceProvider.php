<?php

namespace Reaksmey\KhmerSlug;

use Reaksmey\KhmerSlug\Commands\KhmerSlugCommand;
use Spatie\LaravelPackageTools\Package;
use Spatie\LaravelPackageTools\PackageServiceProvider;

class KhmerSlugServiceProvider extends PackageServiceProvider
{
    public function configurePackage(Package $package): void
    {
        /*
         * This class is a Package Service Provider
         *
         * More info: https://github.com/spatie/laravel-package-tools
         */
        $package
            ->name('laravel-khmer-slug')
            ->hasConfigFile()
            ->hasViews()
            ->hasMigration('create_laravel-khmer-slug_table')
            ->hasCommand(KhmerSlugCommand::class);
    }
}
