print("main module")

import inner
import inner2




if __name__ == '__main__':
    inner.f()
    inner2.innerst.f()
    print(inner._hidden)
