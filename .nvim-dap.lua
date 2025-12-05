local dap = require("dap")


dap.adapters.python = {
    type = 'executable',
    command = 'python3',
    args = { '-m', 'debugpy.adapter' }
}

dap.configurations.python = {
    {
        type = 'python',
        request = 'launch',
        name = "Launch file",
        program = "${file}",
        pythonPath = function()
            return '/home/linuxbrew/.linuxbrew/bin/python3'
        end,
    }
}

dap.adapters.lldb = {
    type = "executable",
    command = "/usr/bin/lldb-vscode-14", -- adjust as needed
    name = "lldb",
}

dap.configurations.rust = {
   {
      name = "wait to attach",
      type = "lldb",
      request = "attach",
      program =  function()
            -- current buffer name
            -- return vim.fn.expand("%"):gsub("%.rs","")
            -- only the file name
            -- return vim.fn.expand("%:t"):gsub("%.rs","")
            -- concat "target/debug/" with the file name
            return "target/debug/day1"
            -- return vim.fn.expand("%"):gsub("%.rs","")
        end,
      waitFor = true
    }
}
