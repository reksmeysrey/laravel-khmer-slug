<?php

namespace Reaksmey\KhmerSlug;

use Bhavingajjar\LaravelPython\LaravelPython;

class KhmerSlug
{
    /**
     * @throws \JsonException
     */
    public function slug(string $str, string $separator = '-')
    {
        $str = trim(str_replace("'", '', $str));
        $pythonSting = (new LaravelPython())
            ->run(__DIR__.'/khmer-nltk/index.py', ["'$str'", $separator]);

        return collect(json_decode($pythonSting, true, 512, JSON_THROW_ON_ERROR))
            ->filter(function ($str) {
                return ! in_array($str, ['', ' '], true);
            })
            ->map(function ($str) {
                return filter_var($str, FILTER_SANITIZE_FULL_SPECIAL_CHARS);
            })->implode($separator);
    }
}
