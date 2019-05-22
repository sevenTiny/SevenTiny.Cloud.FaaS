﻿using System;

namespace Seventiny.Cloud.ScriptEngine.SandBox
{
    internal class ExecutionResult
    {
        public TimeSpan ProcessorTime { get; set; }

        public long TotalMemoryAllocated { get; set; }

        public object ReturnValue { get; set; }
    }
}
