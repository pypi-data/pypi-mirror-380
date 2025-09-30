# JAX Image Tools (JIT) Python API 'pyjit'

## Introduction
The pyjit package contains code common to jit tools, mostly DL and AI tools.
There are common dao packages which each tool consumes to reduce code copying.
These are required 

## Quick Start
### Install

poetry add pyjit


### Usage for Common Tools

from jax.pyjit.dao import StorageKey
This provides an easy way to create json objects used with the JIT server.

### Usage of JIT Client
pyjit will also contain a requests-based client one day similar to the JIT Shell.



