"""
NowPayments currency parsers.

Handles parsing and normalization of NowPayments currency data.
"""

from typing import Optional, Dict, Any, List
from django_cfg.modules.django_logger import get_logger

logger = get_logger("nowpayments_parsers")


class NowPaymentsCurrencyParser:
    """Parser for NowPayments currency data."""
    
    def __init__(self):
        """Initialize currency parser."""
        self.precise_patterns = self._get_precise_patterns()
        self.fallback_patterns = self._get_fallback_patterns()
        self.provider_code_patterns = self._get_provider_code_patterns()
        self.network_suffixes = self._get_network_suffixes()
    
    def parse_currency_code(
        self, 
        provider_code: str, 
        currency_name: str, 
        network_code: Optional[str] = None, 
        ticker: str = ''
    ) -> tuple[str, Optional[str]]:
        """
        Smart parsing using API data, prioritizing ticker field.
        
        Uses ticker as primary source for base currency, then falls back to name parsing.
        
        Examples:
        - "1INCHBSC", "1Inch Network (BSC)", "bsc", "1inch" → ("1INCH", "bsc") 
        - "USDTERC20", "Tether USD (ERC-20)", "eth", "usdt" → ("USDT", "eth") 
        - "BTC", "Bitcoin", "btc", "btc" → ("BTC", "btc")
        """
        # Skip currencies with empty network - they are duplicates
        if network_code is not None and network_code.strip() == "":
            return None, None  # Skip this currency
        
        # Priority 1: Use ticker if available and meaningful
        if ticker and len(ticker.strip()) > 0:
            base_currency = ticker.upper().strip()
            return base_currency, network_code
        
        # Priority 2: Extract from provider code patterns
        base_currency = self.extract_base_currency_from_provider_code(provider_code)
        if base_currency != provider_code:
            return base_currency, network_code
        
        # Priority 3: Extract from name using patterns
        base_currency = self.extract_base_currency_from_name(currency_name, provider_code)
        return base_currency, network_code
    
    def extract_base_currency_from_name(self, currency_name: str, fallback_code: str) -> str:
        """Extract base currency from human-readable name using real API patterns."""
        if not currency_name:
            return fallback_code
        
        name_lower = currency_name.lower()
        
        # Check precise patterns first (most reliable)
        for pattern, base in self.precise_patterns.items():
            if pattern in name_lower:
                return base
        
        # Fallback patterns for edge cases
        for pattern, base in self.fallback_patterns.items():
            if pattern in name_lower:
                return base
        
        # Last resort: use the provider code as-is
        return fallback_code
    
    def extract_base_currency_from_provider_code(self, provider_code: str) -> str:
        """Extract base currency from NowPayments provider code patterns."""
        if not provider_code:
            return provider_code
        
        code_upper = provider_code.upper()
        
        # Check exact matches first
        if code_upper in self.provider_code_patterns:
            return self.provider_code_patterns[code_upper]
        
        # Pattern matching for common suffixes
        for suffix in self.network_suffixes:
            if code_upper.endswith(suffix):
                base_part = code_upper[:-len(suffix)]
                if len(base_part) >= 2:  # Ensure we have a meaningful base
                    return base_part
        
        # Return original if no pattern matches
        return provider_code
    
    def generate_currency_name(
        self, 
        base_currency_code: str, 
        network_code: Optional[str], 
        original_name: str
    ) -> str:
        """Generate proper currency name based on base currency and network."""
        
        # Base currency display names
        base_names = {
            'BTC': 'Bitcoin',
            'ETH': 'Ethereum',
            'USDT': 'Tether USD',
            'USDC': 'USD Coin',
            'BNB': 'Binance Coin',
            'ADA': 'Cardano',
            'DOT': 'Polkadot',
            'MATIC': 'Polygon',
            'AVAX': 'Avalanche',
            'SOL': 'Solana',
            'LTC': 'Litecoin',
            'BCH': 'Bitcoin Cash',
            'XRP': 'Ripple',
            'DOGE': 'Dogecoin',
            'ATOM': 'Cosmos',
            'LINK': 'Chainlink',
            'UNI': 'Uniswap',
            'AAVE': 'Aave',
            'COMP': 'Compound',
            'MKR': 'Maker',
            'SNX': 'Synthetix',
            'YFI': 'yearn.finance',
            'SUSHI': 'SushiSwap',
            'CRV': 'Curve DAO Token',
            'BAL': 'Balancer',
            'REN': 'Ren',
            'KNC': 'Kyber Network',
            'ZRX': '0x',
            'BAT': 'Basic Attention Token',
            'ENJ': 'Enjin Coin',
            'MANA': 'Decentraland',
            'SAND': 'The Sandbox',
            'AXS': 'Axie Infinity',
            'FTM': 'Fantom',
            'ONE': 'Harmony',
            'NEAR': 'NEAR Protocol',
            'ALGO': 'Algorand',
            'XTZ': 'Tezos',
            'EOS': 'EOS',
            'TRX': 'TRON',
            'VET': 'VeChain',
            'THETA': 'Theta Network',
            'FIL': 'Filecoin',
            'ICP': 'Internet Computer',
            'HBAR': 'Hedera',
            'EGLD': 'MultiversX',
            'FLOW': 'Flow',
            'XLM': 'Stellar',
            'IOTA': 'IOTA',
            'XMR': 'Monero',
            'ZEC': 'Zcash',
            'DASH': 'Dash',
            'ETC': 'Ethereum Classic',
            'BSV': 'Bitcoin SV',
            'NEO': 'Neo',
            'QTUM': 'Qtum',
            'ZIL': 'Zilliqa',
            'ONT': 'Ontology',
            'ICX': 'ICON',
            'WAVES': 'Waves',
            'LSK': 'Lisk',
            'NANO': 'Nano',
            'DGB': 'DigiByte',
            'RVN': 'Ravencoin',
            'SC': 'Siacoin',
            'DCR': 'Decred',
            'ZEN': 'Horizen',
            'KMD': 'Komodo',
            'STRAT': 'Stratis',
            'ARK': 'Ark',
            'NXT': 'Nxt',
            'BTS': 'BitShares',
            'STEEM': 'Steem',
            'SBD': 'Steem Dollars',
            'GNT': 'Golem',
            'REP': 'Augur',
            'CVC': 'Civic',
            'STORJ': 'Storj',
            'FUN': 'FunFair',
            'DNT': 'district0x',
            'MCO': 'Monaco',
            'MTL': 'Metal',
            'PAY': 'TenX',
            'REQ': 'Request Network',
            'SALT': 'SALT',
            'SUB': 'Substratum',
            'POWR': 'Power Ledger',
            'ENG': 'Enigma',
            'BNT': 'Bancor',
            'FUEL': 'Etherparty',
            'MAID': 'MaidSafeCoin',
            'AMP': 'Synereo',
            'XAS': 'Asch',
            'PPT': 'Populous',
            'PART': 'Particl',
            'CLOAK': 'CloakCoin',
            'BLOCK': 'Blocknet',
            'NAV': 'NavCoin',
            'VIBE': 'VIBE',
            'LUN': 'Lunyr',
            'KIN': 'Kin',
            'TUSD': 'TrueUSD',
            'PAX': 'Paxos Standard',
            'GUSD': 'Gemini Dollar',
            'HUSD': 'HUSD',
            'BUSD': 'Binance USD',
            'DAI': 'Dai Stablecoin',
            'FRAX': 'Frax',
            'LUSD': 'Liquity USD',
            'SUSD': 'sUSD',
            'USDN': 'Neutrino USD',
            'RSR': 'Reserve Rights',
            'AMPL': 'Ampleforth',
            'TRIBE': 'Tribe',
            'FEI': 'Fei USD',
        }
        
        # Network display names
        network_names = {
            'eth': 'Ethereum',
            'bsc': 'Binance Smart Chain',
            'matic': 'Polygon',
            'arbitrum': 'Arbitrum',
            'optimism': 'Optimism',
            'avalanche': 'Avalanche',
            'fantom': 'Fantom',
            'harmony': 'Harmony',
            'moonbeam': 'Moonbeam',
            'moonriver': 'Moonriver',
            'celo': 'Celo',
            'gnosis': 'Gnosis Chain',
            'aurora': 'Aurora',
            'cronos': 'Cronos',
            'evmos': 'Evmos',
            'milkomeda': 'Milkomeda',
            'syscoin': 'Syscoin NEVM',
            'metis': 'Metis',
            'boba': 'Boba Network',
            'fuse': 'Fuse',
            'telos': 'Telos EVM',
            'kcc': 'KuCoin Community Chain',
            'heco': 'Huobi ECO Chain',
            'okexchain': 'OKEx Chain',
            'xdai': 'xDai',
            'tron': 'TRON',
            'trx': 'TRON',
            'solana': 'Solana',
            'sol': 'Solana',
            'near': 'NEAR Protocol',
            'algorand': 'Algorand',
            'algo': 'Algorand',
            'cardano': 'Cardano',
            'ada': 'Cardano',
            'polkadot': 'Polkadot',
            'dot': 'Polkadot',
            'kusama': 'Kusama',
            'ksm': 'Kusama',
            'cosmos': 'Cosmos Hub',
            'atom': 'Cosmos Hub',
            'osmosis': 'Osmosis',
            'osmo': 'Osmosis',
            'terra': 'Terra',
            'luna': 'Terra',
            'avalanche': 'Avalanche C-Chain',
            'avax': 'Avalanche C-Chain',
            'bitcoin': 'Bitcoin',
            'btc': 'Bitcoin',
            'litecoin': 'Litecoin',
            'ltc': 'Litecoin',
            'bitcoincash': 'Bitcoin Cash',
            'bch': 'Bitcoin Cash',
            'dogecoin': 'Dogecoin',
            'doge': 'Dogecoin',
            'zcash': 'Zcash',
            'zec': 'Zcash',
            'monero': 'Monero',
            'xmr': 'Monero',
            'dash': 'Dash',
            'stellar': 'Stellar',
            'xlm': 'Stellar',
            'ripple': 'Ripple',
            'xrp': 'Ripple',
            'eos': 'EOS',
            'tezos': 'Tezos',
            'xtz': 'Tezos',
            'iota': 'IOTA',
            'miota': 'IOTA',
            'neo': 'Neo',
            'waves': 'Waves',
            'lisk': 'Lisk',
            'lsk': 'Lisk',
            'nano': 'Nano',
            'digibyte': 'DigiByte',
            'dgb': 'DigiByte',
            'ravencoin': 'Ravencoin',
            'rvn': 'Ravencoin',
            'siacoin': 'Siacoin',
            'sc': 'Siacoin',
            'decred': 'Decred',
            'dcr': 'Decred',
            'horizen': 'Horizen',
            'zen': 'Horizen',
            'komodo': 'Komodo',
            'kmd': 'Komodo',
            'stratis': 'Stratis',
            'strat': 'Stratis',
            'ark': 'Ark',
            'nxt': 'Nxt',
            'bitshares': 'BitShares',
            'bts': 'BitShares',
            'steem': 'Steem',
            'vechain': 'VeChain',
            'vet': 'VeChain',
            'theta': 'Theta Network',
            'filecoin': 'Filecoin',
            'fil': 'Filecoin',
            'internetcomputer': 'Internet Computer',
            'icp': 'Internet Computer',
            'hedera': 'Hedera',
            'hbar': 'Hedera',
            'elrond': 'MultiversX',
            'egld': 'MultiversX',
            'flow': 'Flow',
            'zilliqa': 'Zilliqa',
            'zil': 'Zilliqa',
            'ontology': 'Ontology',
            'ont': 'Ontology',
            'icon': 'ICON',
            'icx': 'ICON',
            'qtum': 'Qtum',
            'ethereumclassic': 'Ethereum Classic',
            'etc': 'Ethereum Classic',
            'bitcoinsv': 'Bitcoin SV',
            'bsv': 'Bitcoin SV',
        }
        
        base_name = base_names.get(base_currency_code, base_currency_code)
        
        if not network_code or network_code == base_currency_code.lower():
            # Native currency on its own network
            return base_name
        
        network_name = network_names.get(network_code.lower(), network_code.title())
        return f"{base_name} ({network_name})"
    
    def _get_precise_patterns(self) -> Dict[str, str]:
        """Get precise patterns from real NowPayments API data."""
        return {
            # Stablecoins - most common
            'tether usd': 'USDT',
            'tether (': 'USDT',          # "Tether (Arbitrum One)"
            'tether ': 'USDT',           # "Tether USD (Algorand)"
            'usd coin': 'USDC',          # "USD Coin (Ethereum)"
            'usd coin bridged': 'USDC',  # "USD Coin Bridged (Polygon)"
            'trueusd': 'TUSD',           # "TrueUSD (Tron)"
            'binance usd': 'BUSD',       # "Binance USD (Polygon)"
            'paxos standard': 'PAX',     # "Paxos Standard"
            'gemini dollar': 'GUSD',     # "Gemini Dollar"
            
            # Major cryptocurrencies  
            'bitcoin': 'BTC',
            'ethereum': 'ETH',
            'cardano': 'ADA',
            'dogecoin': 'DOGE',
            'litecoin': 'LTC',
            'bitcoin cash': 'BCH',
            'ripple': 'XRP',
            'polkadot': 'DOT',
            'avalanche': 'AVAX',
            'chainlink': 'LINK',
            'uniswap': 'UNI',
            'ethereum classic': 'ETC',
            'stellar': 'XLM',
            'monero': 'XMR',
            'zcash': 'ZEC',
            'dash': 'DASH',
            'tezos': 'XTZ',
            'cosmos': 'ATOM',
            'algorand': 'ALGO',
            'eos': 'EOS',
            'tron': 'TRX',
            'vechain': 'VET',
            'theta network': 'THETA',
            'filecoin': 'FIL',
            'internet computer': 'ICP',
            'hedera': 'HBAR',
            'multiversx': 'EGLD',
            'elrond': 'EGLD',
            'flow': 'FLOW',
            'near protocol': 'NEAR',
            'solana': 'SOL',
            'fantom': 'FTM',
            'harmony': 'ONE',
            'zilliqa': 'ZIL',
            'ontology': 'ONT',
            'icon': 'ICX',
            'qtum': 'QTUM',
            'waves': 'WAVES',
            'lisk': 'LSK',
            'nano': 'NANO',
            'digibyte': 'DGB',
            'ravencoin': 'RVN',
            'siacoin': 'SC',
            'decred': 'DCR',
            'horizen': 'ZEN',
            'komodo': 'KMD',
            'stratis': 'STRAT',
            'ark': 'ARK',
            'nxt': 'NXT',
            'bitshares': 'BTS',
            'steem': 'STEEM',
            
            # Exchange tokens
            'binance coin': 'BNB',
            'bnb': 'BNB',
            'kucoin shares': 'KCS',
            'huobi token': 'HT',
            'okb': 'OKB',
            'crypto.com coin': 'CRO',
            'ftx token': 'FTT',
            'binance usd': 'BUSD',
            
            # Layer 1/2 tokens
            'polygon': 'MATIC',
            'matic network': 'MATIC',
            'avalanche': 'AVAX',
            'solana': 'SOL',
            'chainlink': 'LINK',
            'uniswap': 'UNI',
            'aave': 'AAVE',
            'compound': 'COMP',
            'maker': 'MKR',
            'synthetix': 'SNX',
            'yearn.finance': 'YFI',
            'sushiswap': 'SUSHI',
            'curve dao token': 'CRV',
            'balancer': 'BAL',
            'ren': 'REN',
            'kyber network': 'KNC',
            '0x': 'ZRX',
            'basic attention token': 'BAT',
            'enjin coin': 'ENJ',
            'decentraland': 'MANA',
            'the sandbox': 'SAND',
            'axie infinity': 'AXS',
            
            # Other stablecoins
            'dai stablecoin': 'DAI',
            'frax': 'FRAX',
            'liquity usd': 'LUSD',
            'susd': 'SUSD',
            'neutrino usd': 'USDN',
            'reserve rights': 'RSR',
            'ampleforth': 'AMPL',
            'tribe': 'TRIBE',
            'fei usd': 'FEI',
            
            # Meme coins
            'shiba inu': 'SHIB',
            'dogecoin': 'DOGE',
            'safemoon': 'SAFEMOON',
            'floki inu': 'FLOKI',
            'baby doge coin': 'BABYDOGE',
            
            # Gaming tokens
            'axie infinity': 'AXS',
            'smooth love potion': 'SLP',
            'the sandbox': 'SAND',
            'decentraland': 'MANA',
            'enjin coin': 'ENJ',
            'gala': 'GALA',
            'illuvium': 'ILV',
            'star atlas': 'ATLAS',
            'yield guild games': 'YGG',
            
            # NFT tokens
            'opensea': 'OS',
            'looks rare': 'LOOKS',
            'x2y2': 'X2Y2',
            
            # Privacy coins
            'monero': 'XMR',
            'zcash': 'ZEC',
            'dash': 'DASH',
            'verge': 'XVG',
            'beam': 'BEAM',
            'grin': 'GRIN',
            
            # Oracle tokens
            'chainlink': 'LINK',
            'band protocol': 'BAND',
            'api3': 'API3',
            'tellor': 'TRB',
            
            # Storage tokens
            'filecoin': 'FIL',
            'storj': 'STORJ',
            'siacoin': 'SC',
            'arweave': 'AR',
            
            # Cross-chain tokens
            'thorchain': 'RUNE',
            'cosmos': 'ATOM',
            'polkadot': 'DOT',
            'kusama': 'KSM',
            'ren': 'REN',
            'anyswap': 'ANY',
            
            # Yield farming tokens
            'yearn.finance': 'YFI',
            'harvest finance': 'FARM',
            'pickle finance': 'PICKLE',
            'cream finance': 'CREAM',
            'alpha finance lab': 'ALPHA',
            
            # Lending tokens
            'aave': 'AAVE',
            'compound': 'COMP',
            'maker': 'MKR',
            'venus': 'XVS',
            'justlend': 'JST',
            
            # Insurance tokens
            'nexus mutual': 'NXM',
            'cover protocol': 'COVER',
            'nsure network': 'NSURE',
            
            # Prediction market tokens
            'augur': 'REP',
            'gnosis': 'GNO',
            'polymarket': 'POLY',
            
            # Social tokens
            'rally': 'RLY',
            'whale': 'WHALE',
            'friends with benefits': 'FWB',
            
            # Fan tokens
            'chiliz': 'CHZ',
            'socios.com': 'CHZ',
            
            # Metaverse tokens
            'decentraland': 'MANA',
            'the sandbox': 'SAND',
            'enjin coin': 'ENJ',
            'bloktopia': 'BLOK',
            'star atlas': 'ATLAS',
            'illuvium': 'ILV',
            'gala': 'GALA',
            'axie infinity': 'AXS',
            'smooth love potion': 'SLP',
            'yield guild games': 'YGG',
            'merit circle': 'MC',
            'ultra': 'UOS',
            'wax': 'WAXP',
            'alien worlds': 'TLM',
            'my neighbor alice': 'ALICE',
            'radio caca': 'RACA',
            'derace': 'DERC',
            'vulcan forged': 'PYR',
            'mobox': 'MBOX',
            'cryptoblades': 'SKILL',
            'thetan arena': 'THG',
            'gods unchained': 'GODS',
            'immutable x': 'IMX',
            'ecomi': 'OMI',
            'veve': 'VVV',
            'efinity token': 'EFI',
            'chromia': 'CHR',
            'phantasma': 'SOUL',
            'wax': 'WAXP',
            'enjin coin': 'ENJ',
            'flow': 'FLOW',
            'dapper labs': 'FLOW',
            'nba top shot': 'FLOW',
            'cryptokitties': 'ETH',
            'cryptopunks': 'ETH',
            'bored ape yacht club': 'ETH',
            'mutant ape yacht club': 'ETH',
            'cool cats': 'ETH',
            'world of women': 'ETH',
            'pudgy penguins': 'ETH',
            'azuki': 'ETH',
            'clone x': 'ETH',
            'moonbirds': 'ETH',
            'otherdeeds for otherside': 'ETH',
            'yuga labs': 'ETH',
        }
    
    def _get_fallback_patterns(self) -> Dict[str, str]:
        """Get fallback patterns for edge cases."""
        return {
            'usdt': 'USDT',
            'usdc': 'USDC', 
            'tusd': 'TUSD',
            'busd': 'BUSD',
            'dai': 'DAI',
            'frax': 'FRAX',
            'btc': 'BTC',
            'eth ': 'ETH',
            'ada': 'ADA',
            'doge': 'DOGE',
            'matic': 'MATIC',
            'avax': 'AVAX',
            'sol': 'SOL',
            'dot': 'DOT',
            'atom': 'ATOM',
            'near': 'NEAR',
            'algo': 'ALGO',
            'xtz': 'XTZ',
            'eos': 'EOS',
            'trx': 'TRX',
            'xlm': 'XLM',
            'xrp': 'XRP',
            'ltc': 'LTC',
            'bch': 'BCH',
            'etc': 'ETC',
            'xmr': 'XMR',
            'zec': 'ZEC',
            'dash': 'DASH',
            'bnb': 'BNB',
            'link': 'LINK',
            'uni': 'UNI',
            'aave': 'AAVE',
            'comp': 'COMP',
            'mkr': 'MKR',
            'snx': 'SNX',
            'yfi': 'YFI',
            'sushi': 'SUSHI',
            'crv': 'CRV',
            'bal': 'BAL',
            'ren': 'REN',
            'knc': 'KNC',
            'zrx': 'ZRX',
            'bat': 'BAT',
            'enj': 'ENJ',
            'mana': 'MANA',
            'sand': 'SAND',
            'axs': 'AXS',
            'ftm': 'FTM',
            'one': 'ONE',
            'zil': 'ZIL',
            'ont': 'ONT',
            'icx': 'ICX',
            'qtum': 'QTUM',
            'waves': 'WAVES',
            'lsk': 'LSK',
            'nano': 'NANO',
            'dgb': 'DGB',
            'rvn': 'RVN',
            'sc': 'SC',
            'dcr': 'DCR',
            'zen': 'ZEN',
            'kmd': 'KMD',
            'strat': 'STRAT',
            'ark': 'ARK',
            'nxt': 'NXT',
            'bts': 'BTS',
            'steem': 'STEEM',
            'vet': 'VET',
            'theta': 'THETA',
            'fil': 'FIL',
            'icp': 'ICP',
            'hbar': 'HBAR',
            'egld': 'EGLD',
            'flow': 'FLOW',
            'iota': 'IOTA',
            'shib': 'SHIB',
            'floki': 'FLOKI',
            'safemoon': 'SAFEMOON',
            'babydoge': 'BABYDOGE',
            'slp': 'SLP',
            'gala': 'GALA',
            'ilv': 'ILV',
            'atlas': 'ATLAS',
            'ygg': 'YGG',
            'rune': 'RUNE',
            'ksm': 'KSM',
            'any': 'ANY',
            'farm': 'FARM',
            'pickle': 'PICKLE',
            'cream': 'CREAM',
            'alpha': 'ALPHA',
            'xvs': 'XVS',
            'jst': 'JST',
            'nxm': 'NXM',
            'cover': 'COVER',
            'nsure': 'NSURE',
            'rep': 'REP',
            'gno': 'GNO',
            'poly': 'POLY',
            'rly': 'RLY',
            'whale': 'WHALE',
            'fwb': 'FWB',
            'chz': 'CHZ',
            'blok': 'BLOK',
            'mc': 'MC',
            'uos': 'UOS',
            'waxp': 'WAXP',
            'tlm': 'TLM',
            'alice': 'ALICE',
            'raca': 'RACA',
            'derc': 'DERC',
            'pyr': 'PYR',
            'mbox': 'MBOX',
            'skill': 'SKILL',
            'thg': 'THG',
            'gods': 'GODS',
            'imx': 'IMX',
            'omi': 'OMI',
            'vvv': 'VVV',
            'efi': 'EFI',
            'chr': 'CHR',
            'soul': 'SOUL',
        }
    
    def _get_provider_code_patterns(self) -> Dict[str, str]:
        """Get NowPayments provider code patterns."""
        return {
            # Stablecoins with network suffixes
            'USDTERC20': 'USDT',
            'USDTTRC20': 'USDT', 
            'USDTBSC': 'USDT',
            'USDTMATIC': 'USDT',
            'USDTARB': 'USDT',
            'USDTALGO': 'USDT',
            'USDTARC20': 'USDT',  # Avalanche
            'USDTOP': 'USDT',     # Optimism
            'USDTSOL': 'USDT',    # Solana
            'USDTTON': 'USDT',    # TON
            'USDTNEAR': 'USDT',   # NEAR
            'USDTEOS': 'USDT',    # EOS
            'USDTDOT': 'USDT',    # Polkadot
            'USDTCELO': 'USDT',   # Celo
            'USDTKAVA': 'USDT',   # Kava
            'USDTXTZ': 'USDT',    # Tezos
            
            # USDC variants
            'USDCERC20': 'USDC',
            'USDCBSC': 'USDC',
            'USDCMATIC': 'USDC',
            'USDCARB': 'USDC',
            'USDCALGO': 'USDC',
            'USDCARC20': 'USDC',  # Avalanche
            'USDCOP': 'USDC',     # Optimism
            'USDCSOL': 'USDC',    # Solana
            'USDCBASE': 'USDC',   # Base
            'USDCKCC': 'USDC',    # KCC
            'USDCXLM': 'USDC',    # Stellar
            
            # ETH variants
            'ETHBSC': 'ETH',
            'ETHARB': 'ETH',
            'ETHBASE': 'ETH',
            'ETHLNA': 'ETH',      # Linea
            
            # Other common patterns
            'BTCBSC': 'BTC',      # Wrapped BTC
            'WBTC': 'BTC',        # Wrapped Bitcoin
            'WETH': 'ETH',        # Wrapped Ethereum
            
            # Network-specific tokens with suffixes
            'BNBBSC': 'BNB',
            'MATICMATIC': 'MATIC',
            'AVAXARC20': 'AVAX',
            'SOLANASOL': 'SOL',
            
            # Additional patterns from NowPayments
            '1INCHBSC': '1INCH',
            '1INCHERC20': '1INCH',
            'AAVEERC20': 'AAVE',
            'AAVEBSC': 'AAVE',
            'ADABSC': 'ADA',
            'ALGOERC20': 'ALGO',
            'APEERC20': 'APE',
            'APEBSC': 'APE',
            'ATOMCOSMOS': 'ATOM',
            'AVAXBSC': 'AVAX',
            'AXSERC20': 'AXS',
            'AXSBSC': 'AXS',
            'BATERC20': 'BAT',
            'BATBSC': 'BAT',
            'BCHBSC': 'BCH',
            'BNBERC20': 'BNB',
            'BUSDBSC': 'BUSD',
            'BUSDERC20': 'BUSD',
            'CAKEBSC': 'CAKE',
            'COMPBSC': 'COMP',
            'COMPERC20': 'COMP',
            'CRVERC20': 'CRV',
            'CRVBSC': 'CRV',
            'DAIBSC': 'DAI',
            'DAIERC20': 'DAI',
            'DOGEERC20': 'DOGE',
            'DOGEBSC': 'DOGE',
            'DOTBSC': 'DOT',
            'DOTERC20': 'DOT',
            'ENJERC20': 'ENJ',
            'ENJBSC': 'ENJ',
            'ETCBSC': 'ETC',
            'ETCERC20': 'ETC',
            'FILBSC': 'FIL',
            'FILERC20': 'FIL',
            'FTMBSC': 'FTM',
            'FTMERC20': 'FTM',
            'GALAERC20': 'GALA',
            'GALABSC': 'GALA',
            'GRTERC20': 'GRT',
            'GRTBSC': 'GRT',
            'ICPERC20': 'ICP',
            'ICPBSC': 'ICP',
            'LINKERC20': 'LINK',
            'LINKBSC': 'LINK',
            'LTCBSC': 'LTC',
            'LTCERC20': 'LTC',
            'MANAERC20': 'MANA',
            'MANABSC': 'MANA',
            'MKRBSC': 'MKR',
            'MKRERC20': 'MKR',
            'NEARERC20': 'NEAR',
            'NEARBSC': 'NEAR',
            'ONEERC20': 'ONE',
            'ONEBSC': 'ONE',
            'SANDERC20': 'SAND',
            'SANDBSC': 'SAND',
            'SHIBERC20': 'SHIB',
            'SHIBBSC': 'SHIB',
            'SNXERC20': 'SNX',
            'SNXBSC': 'SNX',
            'SOLERC20': 'SOL',
            'SOLBSC': 'SOL',
            'SUSHIERC20': 'SUSHI',
            'SUSHIBSC': 'SUSHI',
            'TRXBSC': 'TRX',
            'TRXERC20': 'TRX',
            'TUSDTRC20': 'TUSD',
            'TUSDBSC': 'TUSD',
            'TUSDERC20': 'TUSD',
            'UNIERC20': 'UNI',
            'UNIBSC': 'UNI',
            'VETBSC': 'VET',
            'VETERC20': 'VET',
            'XLMBSC': 'XLM',
            'XLMERC20': 'XLM',
            'XRPBSC': 'XRP',
            'XRPERC20': 'XRP',
            'XTZXTZ': 'XTZ',
            'YFIIERC20': 'YFI',
            'YFIIBSC': 'YFI',
            'ZRXERC20': 'ZRX',
            'ZRXBSC': 'ZRX',
        }
    
    def _get_network_suffixes(self) -> List[str]:
        """Get common network suffixes for pattern matching."""
        return [
            'ERC20', 'TRC20', 'BSC', 'MATIC', 'ARB', 'ALGO', 'ARC20', 
            'OP', 'SOL', 'TON', 'NEAR', 'EOS', 'DOT', 'CELO', 'KAVA', 
            'XTZ', 'BASE', 'KCC', 'XLM', 'LNA', 'AVAX', 'FTM', 'ONE',
            'HARMONY', 'MOONBEAM', 'MOONRIVER', 'GNOSIS', 'AURORA', 
            'CRONOS', 'EVMOS', 'MILKOMEDA', 'SYSCOIN', 'METIS', 'BOBA',
            'FUSE', 'TELOS', 'HECO', 'OKEX', 'XDAI', 'COSMOS', 'OSMOSIS',
            'TERRA', 'KUSAMA', 'POLKADOT', 'CARDANO', 'STELLAR', 'RIPPLE',
            'BITCOIN', 'LITECOIN', 'BITCOINCASH', 'DOGECOIN', 'ZCASH',
            'MONERO', 'DASH', 'TEZOS', 'IOTA', 'NEO', 'WAVES', 'LISK',
            'NANO', 'DIGIBYTE', 'RAVENCOIN', 'SIACOIN', 'DECRED', 
            'HORIZEN', 'KOMODO', 'STRATIS', 'ARK', 'NXT', 'BITSHARES',
            'STEEM', 'VECHAIN', 'THETA', 'FILECOIN', 'INTERNETCOMPUTER',
            'HEDERA', 'ELROND', 'FLOW', 'ZILLIQA', 'ONTOLOGY', 'ICON',
            'QTUM', 'ETHEREUMCLASSIC', 'BITCOINSV'
        ]
