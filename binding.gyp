{
  "targets": [
    {
      "target_name": "pcap_binding",
      "sources": [ "pcap_binding.cc", "pcap_session.cc" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ],
      "link_settings": {
          "libraries": [
              "-lpcap"
          ]
      }
    },
    {
      "target_name": "pcap_binding_package",
      "type": "none",
      "dependencies": [ "pcap_binding" ],
      "copies":
        [ { "destination": "./",
          "files": [ './build/Release/pcap_binding.node' ]
        } ]
    }
  ]
}
