# Extensible DDNS Updater

Pushes the possibly changing IP address of a host myhost.mydomain.com to a remote dynamic domain name service (DDNS).

## Overview
Usage: a cron job would typically be used at regular intervals to run

`sudo <proj-root>/src/lanmanagement/ddns_updater.py <ddns-service-name>`

Assuming the program runs on myhost.mydomain.com, it each time:

1. Detects myhost's current IP address
2. Inquires which IP DNS services currently provide for the host
3. If the two IP addresses differ, updates the DDNS service

A rotating log is maintained at

`<proj-root>/src/lanmanagement/logs/ddns.log<n>`

To obtain a list of supported DDNS services, add the --list (or -l) to the above call.

## Implementation

The out-of-the-box implementation can interact with NameCheap's DDNS service. The files `utils.py` and `dns_service.py` provide DNS related facilities that can be useful for purposes other than dynamic DNS.

### Extending for New DDNS Services

Administrators can extend the implementation to interact with additional DDNS services. The core of these service interactions is to generate a proper URL that instructs the service to update its IP address for `myhost.mydomain.com/.net.io,...` For each supported service the query parameters are stored as a section of options in a Python `configparser` `.ini` file. Like this:

```ini
[namecheap]

# Part of URL for updating service before the query parms:
url_root     = https://dynamicdns.park-your-domain.com/update?
secrets_file = $HOME/.ssh/ddns_password
# The query parameters:
host         = myhost
domain       = mydomain.net
```

Other services might require additional information.

The administrator creates a short subclass, such as `NameCheap` in `ddns_service_adapters.py`. The class just needs to provide a single method `ddns_update_url(new_ip),` which returns a URL suitable to send to the new DDNS service for IP update.

### Architecture

The main class is `DDNSUpdater`. Its constructor takes a DDNS servicename, such as "namecheap". That name is provided as argument when `ddns_updater.py` is run on the command line, or in a `cron` job.

<div align="center">
  <img src="https://raw.githubusercontent.com/paepcke/ddns-updater/main/readme_architecture.png"
       alt="DDNS service update architecture"
       width="400px"
       >
</div>

The `DDNSUpdater` requests a handler for the respective DDNS service from a singleton instance of class `DDNSServiceManager`. This returned handler will be an instance of the subclass mentioned in [Extending for New DDNS Services ](#extending-for-new-ddns-services). The `DDNSUpdater` then calls `ddns_update_url()` on the handler whenever it determines that the host's IP address has changed. It issues an HTTP request using the returned URL.
