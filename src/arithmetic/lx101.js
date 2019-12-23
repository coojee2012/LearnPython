const dns = require('dns');


dns.lookup('b8b735d76a75ade2.complispace.me', (err, address, family) => {
  console.log('IP 地址: %j 地址族: IPv%s', address, family);
});
