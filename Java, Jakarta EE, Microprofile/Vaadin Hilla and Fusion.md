These are Vaadin's client-side front ends calling Java backends. **Fusion** (Lit/TypeScript) was renamed and reworked into **Hilla** (Spring Boot + React). The server-side framework is in [Vaadin Flow](Vaadin%20Flow.md).

## Hilla
### Java endpoints
TypeScript clients are generated for these classes:
```java
@BrowserCallable              // older name: @Endpoint
@AnonymousAllowed             // endpoints are secured (deny all) by default
public class HoardService {
    public BigDecimal addGold(long hoardNumber, BigDecimal coins) { ... }
}
```
Methods inherited from a base class are not exposed unless the base class is annotated with `@EndpointExposed`.

### Reactive endpoints
Return a `Flux`, or an `EndpointSubscription`, which wraps a `Flux` and lets you run code when the client unsubscribes:
```java
public Flux<@NonNull String> goldPrice() {
    return Flux.interval(Duration.ofSeconds(1)).onBackpressureDrop()
        .map(tick -> currentGoldPrice().toString());
}

public EndpointSubscription<@NonNull String> goldPriceCancellable() {
    return EndpointSubscription.of(goldPrice(), () -> LOGGER.info("A dragon stopped watching the gold price"));
}
```
```tsx
import { useSignal } from '@vaadin/hilla-react-signals';
import { Subscription } from '@vaadin/hilla-frontend';
import { Button, TextField } from '@vaadin/react-components';
import { goldPriceCancellable } from 'Frontend/generated/HoardService';

export default function GoldPriceView() {
  const price = useSignal('');
  const subscription = useSignal<Subscription<string> | undefined>(undefined);

  const toggle = () => {
    if (subscription.value) {                       // check .value, the signal object itself is always truthy
      subscription.value.cancel();
      subscription.value = undefined;
    } else {
      subscription.value = goldPriceCancellable().onNext(p => { price.value = p; });   // also onError, onComplete
    }
  };

  return (
    <section className="flex p-m gap-m items-end">
      <TextField label="Gold price" value={price.value} readonly />
      <Button onClick={toggle}>Toggle</Button>
    </section>
  );
}
```

### Client middleware
A middleware intercepts every endpoint call, much like a servlet filter on the client:
```typescript
import { Middleware, MiddlewareContext, MiddlewareNext } from '@vaadin/hilla-frontend';

export const LogMiddleware: Middleware = async (context: MiddlewareContext, next: MiddlewareNext) => {
  const { endpoint, method, params } = context;
  console.log(`${endpoint}.${method}(${JSON.stringify(params)})`);

  // you can replace the request (a Fetch API Request)...
  context.request = new Request(context.request.url.replace('https://dragonbank.example', 'https://backup.dragonbank.example'), context.request);

  const response: Response = await next(context);   // ...or return your own Response without calling next
  console.log(`${response.status} ${response.statusText}`);
  return response;
};
```
Registering it:
```typescript
// your own client
const client = new ConnectClient({ prefix: '/connect', middlewares: [LogMiddleware] });
// or the generated one
import client from 'Frontend/generated/connect-client.default';
client.middlewares = [LogMiddleware];
```

### File-based routing
Views go in `src/main/frontend/views`:

| File name | Meaning |
|---|---|
| `@index.tsx` | index page of the directory |
| `@layout.tsx` | layout for the routes in the same directory and its subdirectories; renders `<Outlet />` |
| `{hoardNumber}.tsx` | required parameter |
| `{{hoardNumber}}.tsx` | optional parameter |
| `{...path}.tsx` | wildcard |
| `_helper.tsx` | ignored by the router (leading underscore) |

```tsx
import { useParams } from 'react-router';
const { hoardNumber } = useParams();
const { '*': path } = useParams();       // React Router always names the wildcard "*"
```
**A menu built from the routes:**
```tsx
import { createMenuItems } from '@vaadin/hilla-file-router/runtime.js';
import { SideNav, SideNavItem, Icon } from '@vaadin/react-components';
import { useNavigate, useLocation } from 'react-router';

export default function MainMenu() {
  const navigate = useNavigate();
  const location = useLocation();
  return (
    <SideNav onNavigate={({ path }) => path && navigate(path)} location={location}>
      {createMenuItems().map(({ to, icon, title }) => (
        <SideNavItem path={to} key={to}>
          {icon && <Icon icon={icon} slot="prefix" />}
          {title}
        </SideNavItem>
      ))}
    </SideNav>
  );
}
```

---

## Fusion (legacy: Lit + TypeScript)
### A Lit component
```ts
import { LitElement, html } from 'lit';
import { customElement, state, query } from 'lit/decorators.js';
import '@vaadin/vaadin-button/vaadin-button';           // import the Vaadin web components you use

@customElement('greeting-view')
export class GreetingView extends LitElement {
  @state() private name = '';                           // re-renders on change
  @state() private notificationOpen = false;
  @query('#greeting') private notification: any;        // reference to an element in the template

  render() {
    return html`
      <vaadin-vertical-layout theme="padding">
        <vaadin-text-field label="Dragon name"
            @value-changed=${(e: any) => this.name = e.detail.value}></vaadin-text-field>
        <vaadin-combo-box placeholder="Cave" .items=${['North Peak', 'Lava Lake']}></vaadin-combo-box>
        <vaadin-button @click=${this.greet}>
          <iron-icon icon="vaadin:check"></iron-icon> Greet
        </vaadin-button>
        <vaadin-notification id="greeting" .renderer=${this.greetingRenderer}></vaadin-notification>
      </vaadin-vertical-layout>`;
  }

  greet() { this.notification.open(); }   // or, without @query: bind .opened=${this.notificationOpen} and set this.notificationOpen = true
  greetingRenderer = (root: HTMLElement) => { root.textContent = `Welcome, ${this.name}!`; };
}
```
### Mixing with server-side views
- Create `index.html` and `index.ts` in the `frontend` directory (its location depends on the packaging). The easiest way is to copy the generated ones from `target`.
- Make the styles consistent with the server-side views. In `index.html`: `<custom-style><style include="lumo-typography"></style></custom-style>`. In `index.ts`: `import '@vaadin/vaadin-lumo-styles/all-imports';`.
- Define the client routes in `index.ts`:
```ts
import './greeting-view';
const routes = [
  { path: 'greeting', component: 'greeting-view' },
  ...serverSideRoutes          // MUST be the last entry
];
```
