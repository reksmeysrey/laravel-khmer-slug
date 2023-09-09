<?php

namespace Reaksmey\KhmerSlug\Commands;

use Illuminate\Console\Command;

class KhmerSlugCommand extends Command
{
    public $signature = 'laravel-khmer-slug';

    public $description = 'My command';

    public function handle(): int
    {
        $this->comment('All done');

        return self::SUCCESS;
    }
}
