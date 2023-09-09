<?php

namespace Reaksmey\KhmerSlug\Facades;

use Illuminate\Support\Facades\Facade;

/**
 * @see \Reaksmey\KhmerSlug\KhmerSlug
 */
class KhmerSlug extends Facade
{
    protected static function getFacadeAccessor()
    {
        return \Reaksmey\KhmerSlug\KhmerSlug::class;
    }
}
