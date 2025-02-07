# CodeNames

## Running on Testnet
- For validator
`python neurons/validator.py --subtensor.network test --wallet.name test_validator --wallet.hotkey h1 --netuid 250 --logging.info`

using pm2:

`pm2 start neurons/validator.py --interpreter python --name test-validator-1 -- \
--subtensor.network test \
--wallet.name test_validator \
--wallet.hotkey h1 \
--netuid 250 \
--logging.info`


- For Miner (miner uid : 1)
`python neurons/miner.py --subtensor.network test --wallet.name test_miner --wallet.hotkey h1 --netuid 250 --logging.info`