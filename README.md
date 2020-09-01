# commentWriter
A long time ago in a startup far far away one Dr. Aaron Goldman described to me a theoretical blobstore
backed by comments and messagebord posts. I'm not sure how far I want to take it, but that really
captured my imagination and I'd like to find a way to do that in a way that doesn't rely on 
maintainers/admins just not noticing massive base64 blobs in the comments/messages. I would
instead prefer to rely on being kind to others, and people not minding that a kind person chooses
to include some amount of random ascii stuff in their posts (first thought: format arbitrary data
chunks like a PGP Signature? but people don't normally sign internet comments. Maybe make bot say 
they're sharing coupon/referral codes or something and format the chunked data like that?)
