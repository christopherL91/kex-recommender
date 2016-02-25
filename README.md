#   Recommender engine

### Automatic experiments using Graphlab and Docker

This is the automatic experiments script for our bachelor thesis about
recommender engines.

### Install instructions:

*	Download the movielenz datset
*   Get access to Graphlab create and run

```
 cat docker-template | env MAIL=graphlab-mail \
 	PASS=graphlab-password envsubst > Dockerfile
	docker build -t 'recommender-engine' .
	docker run -it --rm recommender-engine --help
```

LICENSE: MIT
