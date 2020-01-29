class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        r = re.compile(f'{"[a-z]*".join(["", *pattern, ""])}$')
        return map(r.match, queries)