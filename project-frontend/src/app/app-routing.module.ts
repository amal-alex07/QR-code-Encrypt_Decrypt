import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { EncryptionComponent } from './encryption/encryption.component';
import { DecryptionComponent } from './decryption/decryption.component';
import { PreviewComponent } from './preview/preview.component'
import { DisplayComponent } from './display/display.component'

const routes: Routes = [
   { path: '', component: LoginComponent },
   { path: 'home', component: HomeComponent },
   { path: 'encryption', component:EncryptionComponent },
   { path: 'decryption', component:DecryptionComponent  },
   { path: 'preview', component: PreviewComponent},
   { path: 'display', component: DisplayComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]

})
export class AppRoutingModule { }
