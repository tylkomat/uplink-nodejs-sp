{
  'conditions':[
    ['OS=="linux"',{
      'targets':[
        {
          "target_name": "uplink",
          "include_dirs": ["./functions"],
          "sources":["./libUplink.cc", "./functions/promises_execute.cc", "./functions/promises_complete.cc", "./functions/project_operations.cc", "./functions/download_operations.cc", "./functions/upload_operations.cc", "./functions/access_operations.cc", "./functions/bucket_operations.cc", "./functions/object_operations.cc", "./functions/release_objects_helpers.cc"],
          "libraries":["-L/<(module_root_dir)", "-luplinkcv1.7.0"],
          "cflags_cc": ["-fexceptions","-fPIC","-Wno-unknown-pragmas"]
        }
      ]
    }],
    ['OS=="win"',{
      'targets':[
        {
          "target_name": "uplink",
          "include_dirs": ["./functions_win"],
          "sources":["libUplink_win.cc" , "./functions_win/promises_execute_win.cc", "./functions_win/promises_complete_win.cc", "./functions_win/project_operations_win.cc", "./functions_win/download_operations_win.cc", "./functions_win/upload_operations_win.cc", "./functions_win/access_operations_win.cc", "./functions_win/bucket_operations_win.cc", "./functions_win/object_operations_win.cc"],
          "copies":[{
            "destination":"<(module_root_dir)/build/Release",
            "files":["<(module_root_dir)/libuplinkcversion.h","<(module_root_dir)/libuplinkcv1.7.0.dll","<(module_root_dir)/libuplinkcv1.7.0.h","<(module_root_dir)/uplink_definitions.h","<(module_root_dir)/uplink_combat.h"]
          }],
          "ldflags":["-Wl,-rpath","build/Release"],
        },
      ]
    }],
    ['OS=="mac"',{
        'targets':[
          {
            "target_name": "uplink",
            'include_dirs': ['<(module_root_dir)', "./functions"],
            "sources":["./libUplink.cc", "./functions/promises_execute.cc", "./functions/promises_complete.cc", "./functions/project_operations.cc", "./functions/download_operations.cc", "./functions/upload_operations.cc", "./functions/access_operations.cc", "./functions/bucket_operations.cc", "./functions/object_operations.cc", "./functions/release_objects_helpers.cc"],
            "link_settings": {
              "libraries":["-L/<(module_root_dir)", "-luplinkcv1.7.0"],
            },
            "cxxflags":["-fPIC"],
            "cflags_cc": ["-fexceptions","-fPIC","-Wno-unknown-pragmas"],
          }
        ]
    }]
  ]
}